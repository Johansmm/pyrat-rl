"""This program controls a PyRat player by performing manh actions.

More precisely, at each turn, the program follows the cheese closest to it.
"""

import numpy as np

from src.ai_tools import decorator, Location


@decorator.turn
def turn(maze_width, maze_height, name, player_locations, cheese, possible_actions):
    """Return the action that a Manhattan agent would do: go for the nearest cheese

    Parameters
    ----------
    maze_width : int
        Width of the maze in number of cells.
    maze_height : int
        Height of the maze in number of cells.
    name : str
        Name of the player controlled by this function.
    player_locations : Dict[str, int]
        Locations for all players in the game.
    cheese : List[int]
        List of available pieces of cheese in the maze.
    possible_actions : List[str]
        List of possible actions.

    Returns
    -------
    str
        The action taken by the program (one of ``possible_actions``).
    """
    player_loc = Location(player_locations[name], width=maze_width, height=maze_height)
    lower_distance = np.inf

    # Compute the nearest cheese
    for poc in cheese:
        distance = player_loc.compute_distance(poc)
        if distance < lower_distance:
            lower_distance = distance
            closer_cheese = poc
    return player_loc.choose_action(closer_cheese, possible_actions)
