__all__ = ["Location"]

from enum import Enum, auto


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
