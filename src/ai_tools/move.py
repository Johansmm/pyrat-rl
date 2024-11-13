__all__ = ["Location"]

from enum import Enum, auto
import numpy as np


def value_to_location(check_maze=False):
    def decorator(fn):
        def process_value(self, *values):
            lvalues = []
            for value in values:
                if not isinstance(value, Location):
                    value = Location(value, self.width, self.height)
                lvalues.append(value)
            if check_maze:
                if self.height is None or self.width is None:
                    raise ValueError(
                        f"Maze width/height must be defined when calling '{fn.__name__}'."
                    )
                if any(self.width != v.width or self.height != v.height for v in lvalues):
                    str_values = [str(self)] + [str(loc) for loc in lvalues]
                    raise ValueError(
                        f"Unsupported {fn.__name__}({', '.join(str_values)}): "
                        "Maze sizes must be equal."
                    )
            return fn(self, *lvalues)

        return process_value

    return decorator


class Moves(Enum):
    nothing = 0
    up = auto()
    right = auto()
    down = auto()
    left = auto()


class Location:
    """Define a location in a maze

    Parameters
    ----------
    loc : Union[int, Location]
        Location described by an index in the maze (int)
    width : int, optional
        The maze width, by default None
    height : int, optional
        The maze height, by default None
    """

    def __init__(self, loc, width=None, height=None):
        self.width = width
        self.height = height
        self.loc = loc

    @property
    def loc(self):
        return self._loc

    @loc.setter
    def loc(self, new_loc):
        if isinstance(new_loc, Location):
            if self.height is None:
                self.height = new_loc.height
            if self.width is None:
                self.width = new_loc.width
            _loc = new_loc.loc
        else:
            try:
                _loc = int(new_loc)
                assert _loc == new_loc, "Location must be integer."
            except Exception as e:
                raise ValueError(f"Unrecognized {new_loc}. Detail:{str(e)}.")
        self._loc = _loc

    @property
    @value_to_location(check_maze=True)
    def coordinates(self):
        return np.divmod(self.loc, self.width)[::-1]

    def compute_distance(self, other):
        """Calculate the distance between locations

        Parameters
        ----------
        other : Location
            Second location to compute distance
        """
        x, y = self.__sub__(other)
        return abs(x) + abs(y)

    def choose_action(self, target, possible_actions=None):
        """Choose the action that the agent must take to reach the target

        Given that one agent only moves once and can't move diagonally, it suffices to move in
        the direction of the target, moving vertically first and then horizontally

        Parameters
        ----------
        target : Location
            Target location
        possible_actions : List[str], optional
            List of possible actions, by default None

        Returns
        -------
        str
            The suggested action
        """
        if possible_actions is None:
            possible_actions = list(Moves.__members__)
        dx, dy = self.__sub__(target)
        if dy < 0:
            return possible_actions[Moves.up.value]
        if dy > 0:
            return possible_actions[Moves.down.value]
        if dx < 0:
            return possible_actions[Moves.right.value]
        if dx > 0:
            return possible_actions[Moves.left.value]
        # We are in the target !
        return possible_actions[Moves.nothing.value]

    def play_action(self, action: str, possible_actions: list[str] = None):
        """Update location with the desired action

        Parameters
        ----------
        action : str
            One of `possible_actions`
        possible_actions : List[str], optional
            List of possible actions, by default None

        Returns
        -------
        Location
            The updated location
        """
        if possible_actions is None:
            possible_actions = list(Moves.__members__)

        delta = 0
        x, y = self.coordinates
        match possible_actions.index(action):
            case Moves.up.value:
                if y > 0:
                    delta = -self.width
            case Moves.down.value:
                if y < self.height - 1:
                    delta = self.width
            case Moves.right.value:
                if x < self.width - 1:
                    delta = 1
            case Moves.left.value:
                if x > 0:
                    delta = -1
        return Location(self.loc + delta, self.width, self.height)

    @value_to_location()
    def __eq__(self, value):
        return repr(self) == repr(value)

    @value_to_location(check_maze=True)
    def __sub__(self, value):
        x, y = self.coordinates
        xv, yv = value.coordinates
        return (x - xv, yv - y)

    def __repr__(self):
        return f"Location({self.loc}, {self.width}, {self.height})"
