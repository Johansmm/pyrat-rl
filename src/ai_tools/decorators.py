__all__ = ["decorator"]

from functools import wraps


def _handle_arguments(func, arg_names, /, *args, **kwargs):
    # Sanitize: check arguments are in arg_names
    for name in kwargs:
        if name not in arg_names:
            raise TypeError(f"{func.__name__} got an unexpected keyword argument '{name}'")
    # Clean arguments: transfer only those were defined by func
    full_kwargs = {**{k: v for k, v in zip(arg_names[:len(args)], args)}, **kwargs}
    new_kwargs = {k: v for k, v in full_kwargs.items() if k in func.__code__.co_varnames}
    return new_kwargs


class decorator:
    """Class that embeds the different decorators
    """
    @staticmethod
    def preprocessing(func):
        """Decorator that removes parameters that are not used by preprocessing

        Example:
            >>> @decorator.preprocessing
            >>> def preprocessing(maze):
            >>>     # Allow to write this function without the other preprocessing parameters,
            >>>     # because it just need of 'maze'.

        Parameters
        ----------
        func : callable
            the function to decorate

        Returns
        -------
        callable
            the wrapped function
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_names = ['maze', 'maze_width', 'maze_height', 'name', 'teams',
                         'player_locations', 'cheese', 'possible_actions', 'memory']
            new_kwargs = _handle_arguments(func, arg_names, *args, **kwargs)
            return func(**new_kwargs)
        return wrapper

    @staticmethod
    def postprocessing(func):
        """Decorator that removes parameters that are not used by postprocessing

        Example:
            >>> @decorator.postprocessing
            >>> def postprocessing(possible_actions):
            >>>     # Allow to write this function without the other postprocessing parameters,
            >>>     # because it just need of 'possible_actions'.

        Parameters
        ----------
        func : callable
            the function to decorate

        Returns
        -------
        callable
            the wrapped function
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_names = ['maze', 'maze_width', 'maze_height', 'name', 'teams', 'player_locations',
                         'player_scores', 'player_muds', 'cheese', 'possible_actions', 'memory',
                         'stats']
            new_kwargs = _handle_arguments(func, arg_names, *args, **kwargs)
            return func(**new_kwargs)
        return wrapper

    @staticmethod
    def turn(func):
        """Decorator that removes parameters that are not used by turn

        Example:
            >>> @decorator.turn
            >>> def turn(maze, player_locations):
            >>>     # Allow to write this function without the other turn parameters,
            >>>     # because it just need of 'maze' and 'player_locations'.

        Parameters
        ----------
        func : callable
            the function to decorate

        Returns
        -------
        callable
            the wrapped function
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_names = ['maze', 'maze_width', 'maze_height', 'name', 'teams', 'player_locations',
                         'player_scores', 'player_muds', 'cheese', 'possible_actions', 'memory']
            new_kwargs = _handle_arguments(func, arg_names, *args, **kwargs)
            return func(**new_kwargs)
        return wrapper
