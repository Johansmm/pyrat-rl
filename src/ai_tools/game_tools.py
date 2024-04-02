__all__ = ["update_scores"]


def update_scores(player_locations, player_scores, cheeses):
    """Update player scores

    Each player win +1 point iff they are alone on the square with a cheese.
    If several players are in the same square and there is a cheese on it,
    each player gets `1 - (num_players_in_square - 1)/total_players` points.

    Parameters
    ----------
    player_locations : Dict[str, Location]
        Locations for all players in the game.
    player_scores : Dict[str, float]
        Scores for all players in the game
    cheeses : List[int]
        List of remaining cheeses

    Returns
    List[Location]
        Cheeses that were not consumed
    """
    # Each player in cheese wins 1.0 point
    total_players = len(player_locations)
    remaining_cheeses = list(cheeses)
    for cheese in cheeses:
        players_in_target = [k for k, v in player_locations.items() if v == cheese]
        if len(players_in_target) > 0:
            remaining_cheeses.remove(cheese)
        for player_name in players_in_target:
            player_scores[player_name] += 1 - (len(players_in_target) - 1) / total_players
    return remaining_cheeses
