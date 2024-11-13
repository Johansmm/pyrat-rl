import pytest

from src.ai_tools.move import Location, value_to_location


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


@pytest.mark.parametrize(
    "x, y",
    [
        [Location(5), 5],
        [Location(7), Location(7)],
        [Location(5, 10, 12), 5],
        [Location(9, 12, 12), Location(9, 12, 12)],
    ],
    ids=["sloc-int", "sloc-sloc", "loc-int", "loc-loc"],
)
def test_location_eq(x, y):
    assert x == y


@pytest.mark.parametrize(
    "x, y, expected",
    [[Location(5, 10, 10), 5, (0, 0)], [Location(99, 10, 10), Location(54, 10, 10), (5, -4)]],
    ids=["loc-int", "loc-loc"],
)
def test_location_sub(x, y, expected):
    assert (x - y) == expected


@pytest.mark.parametrize(
    "loc, expected",
    [
        [Location(5), "Location(5, None, None)"],
        [Location(4, height=10, width=5), "Location(4, 5, 10)"],
    ],
    ids=["index", "loc"],
)
def test_repr(loc, expected):
    assert repr(loc) == expected


@pytest.mark.parametrize("num_imputs", [0, 2, 4])
@pytest.mark.parametrize("check_maze", [True, False])
def test_value_to_location(num_imputs, check_maze):
    def fn(*locs):
        assert len(locs) > 0
        # Check locatio types are changed to Location
        assert all(isinstance(loc, Location) for loc in locs)
        return locs[0].loc

    main_loc = Location(9, 5, 2)
    other_locs = [Location(i, 5, 2) if i % 2 == 0 else i for i in range(num_imputs)]

    # Decorate fn to convert all arguments in locs implicitly
    decorated_fn = value_to_location(check_maze=check_maze)(fn)

    # Call decorated fn
    y = decorated_fn(main_loc, *other_locs)
    assert isinstance(y, int)


def test_value_to_location_ko():
    def my_fn(*args):
        pass

    decorated_fn = value_to_location(check_maze=True)(my_fn)

    with pytest.raises(ValueError, match="Maze width/height must be defined when calling 'my_fn'"):
        main_loc = Location(9)
        decorated_fn(main_loc, Location(1), Location(2), Location(3))

    with pytest.raises(ValueError, match="Maze sizes must be equal"):
        decorated_fn(Location(9, 2, 10), Location(1, 10, 2))
