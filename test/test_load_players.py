import sys
import pytest

from src import load_players

from .conftest import from_path_to_program


@pytest.fixture(scope="session")
def unsupported_program(tmp_path_factory):
    programm = """# Unsupported program: it does not define turn()!"""
    program_path = tmp_path_factory.mktemp("programs") / "unsupported.py"
    with open(program_path, "w") as f:
        f.write(programm)

    # Include base directory in sys.path, enabling to recognize program by importlib
    sys.path.append(program_path.parts[0])
    return from_path_to_program(program_path)


def test_load_player(random_ai):
    player = load_players([random_ai])[0]

    assert player["preprocessing_function"] is None
    assert player["postprocessing_function"] is None

    # Run a fake turn: this program choose a random action
    possible_actions = ['R', 'L', 'U', 'D']
    action = player["turn_function"](possible_actions=possible_actions)
    assert action in possible_actions


def test_load_multiplayers(random_ai):
    players = load_players([random_ai] * 3)

    # Each player is load in different teams
    for team_id, player in zip(range(1, len(players) + 1), players):
        team_name = f"team_{team_id}"
        player_name = random_ai.split(".")[-1]
        assert player["team"] == team_name
        assert player["name"] == f"{team_name}:{player_name}"


def test_load_players_ko(unsupported_program):
    with pytest.raises(AttributeError, match="Unsupported player: (.*) has no attribute"):
        load_players([unsupported_program])
