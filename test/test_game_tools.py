import pytest

from src.ai_tools import update_scores, Location


@pytest.mark.parametrize(
    "locations, scores, cheeses, final_scores, exp_remaining_cheeses",
    [
        ((Location(5), 4), (0.0, 5.0), [4, Location(1)], (0.0, 6.0), [Location(1)]),
        ((Location(2), Location(2)), (1.5, 1.5), [Location(2), Location(1)], (2.0, 2.0), [1]),
        ((1, 2, 2), (0.5, 1 / 3, 4 / 3), [1, 2], (1.5, 1.0, 2.0), []),
        ((2, 2, 3, 4), (0.5, 0.75, 1.0, 0.0), [2, 4, 1], (1.25, 1.5, 1.0, 1.0), [1]),
    ],
    ids=["2-players", "2-players-draw", "3-players", "4-players"],
)
def test_update_scores(locations, scores, cheeses, final_scores, exp_remaining_cheeses):
    player_locations = {f"player_{key}": x for key, x in enumerate(locations)}
    player_scores = {f"player_{key}": x for key, x in enumerate(scores)}
    final_scores = {f"player_{key}": x for key, x in enumerate(final_scores)}
    remaining_cheeses = update_scores(player_locations, player_scores, cheeses)
    assert remaining_cheeses == exp_remaining_cheeses
    assert player_scores == final_scores
