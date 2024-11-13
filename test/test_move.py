import pytest

from src.ai_tools.move import Location


@pytest.mark.parametrize(
    "loc, w, h",
    [
        (105, 12, 15),
        (-10, 12, 15),
        (Location(5, 10, 10), None, None),
        (Location(7, 12), None, 11),
        (Location(10, None, 12), 12, None),
    ],
    ids=["pos", "neg", "loc1", "loc2", "loc3"],
)
def test_location(loc, w, h):
    location = Location(loc, width=w, height=h)
    assert isinstance(location.loc, int)
    assert location.width == (w or loc.width if isinstance(loc, Location) else w)
    assert location.height == (h or loc.height if isinstance(loc, Location) else h)


def test_location_ko():
    with pytest.raises(ValueError, match="Unrecognized"):
        Location((1, 2))

    with pytest.raises(ValueError, match="must be integer"):
        Location(5.2)
