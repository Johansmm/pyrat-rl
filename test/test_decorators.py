import pytest
import pickle

from src.ai_tools.decorators import decorator, _handle_arguments


def test_handled_arguments():
    def func_to_wrapper(arg1, kwarg1=None):
        return {"arg": arg1, "kwarg": kwarg1}

    arg_names, args = ["arg1", "arg2", "kwarg1", "kwarg2"], (5, 10)
    kwargs = {"kwarg1": "value", "kwarg2": "removed_value"}

    # Following a function signature, handle_arguments removes the incompatible arguments
    new_kwargs = _handle_arguments(func_to_wrapper, arg_names, *args, **kwargs)
    assert "arg2" not in new_kwargs and "kwarg2" not in new_kwargs

    # Check function could be called with new kwargs
    result = func_to_wrapper(**new_kwargs)
    assert result["arg"] == args[0] and result["kwarg"] == kwargs["kwarg1"]

    # Check handle_arguments raise an exception when passing an argument outside of arg_names
    with pytest.raises(TypeError, match="got an unexpected keyword"):
        _handle_arguments(func_to_wrapper, arg_names, unsupported_arg="value")


@pytest.mark.parametrize("decorator_fn, num_args",
                         [(decorator.preprocessing, 9),
                          (decorator.postprocessing, 12),
                          (decorator.turn, 11)],
                         ids=["preprocessing", "postprocessing", "turn"])
def test_decorators(decorator_fn, num_args):
    # We must instance fake_fn globally to avoid local references, incompatible with pickle
    global fake_fn

    @decorator_fn
    def fake_fn(maze, maze_width, player_locations, possible_actions=["R", "L"]):
        assert maze_width == 10
        assert maze == "maze"
        assert player_locations == "loc"
        assert isinstance(possible_actions, list)

    # Each decorator is in charge to remove the parameters not present in target function
    kwargs = {"maze": "maze", "player_locations": "loc", "possible_actions": [0] * num_args}
    fake_fn(maze_width=10, maze_height=20, **kwargs)

    # Call function with full arguments
    args = (10,) * (num_args - 3)
    fake_fn(*args, **kwargs)

    # Important behavior: fake_fn must be serializable (requirement required by pyrat)
    pickle.dumps(fake_fn)
