__all__ = ["load_players"]

import os
import importlib


def load_players(program_names):
    """Load a list of players into the memory

    Parameters
    ----------
    program_names : List[str]
        The programs to load

    Returns
    -------
    List[Dict]
        The player list to run a pyrat game
    """
    players = []
    for idx, player_path in enumerate(program_names):
        player = importlib.import_module(player_path)
        player_spec = player.__spec__.origin
        try:
            player_turn_fn = player.turn
        except AttributeError as error:
            raise AttributeError(f"Unsupported player: {str(error)}")
        team_name = f"team_{idx+1}"
        players.append(
            {
                "name": f"{team_name}:{os.path.splitext(os.path.basename(player_spec))[0]}",
                "team": team_name,
                "preprocessing_function": player.__dict__.get("preprocessing", None),
                "turn_function": player_turn_fn,
                "postprocessing_function": player.__dict__.get("postprocessing", None),
            }
        )
    return players
