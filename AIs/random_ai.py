""" This program controls a PyRat player by performing random actions.

More precisely, at each turn, a random choice among all possible actions is selected.
Note that this doesn't take into account the structure of the maze.
"""

import random
from src.ai_tools import decorator


@decorator.turn
def turn(possible_actions,):
    """ Return a random action from the possible ones.

    Parameters
    ----------
    possible_actions : List[str]
        List of possible actions.

    Returns
    -------
    str
        The action taken by the program (one of ``possible_actions``).
    """
    return random.choice(possible_actions)
