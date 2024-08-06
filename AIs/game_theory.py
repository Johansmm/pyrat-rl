"""This program controls a PyRat player by performing combinatorial game theory against
a greedy opponent.

Knowing the opponent's behavior, it calculates the move set that allows him to obtain
the highest possible score.

For this reason the computation is costly, which increases with the number of target cheeses.
"""

from collections import namedtuple

from src.ai_tools import update_scores, Location, decorator

from . import manh

GameInfo = namedtuple(
    "GameInfo", ["player_locations", "player_scores", "cheeses", "possible_actions"]
)


def simulate_game_until_target(target, name, current_game):
    """Simulate what will happen until some agent reach the target

    Parameters
    ----------
    cheese_target : Location
        Cheese to be reached for agents
    name : str
        Name of the player controlled by this function.
    current_game : GameInfo
        Current status of the game

    Returns
    -------
    GameInfo :
        End state of the game until reache the target
    """
    # Clone locations and scores to avoid modifying initial values
    player_locations = current_game.player_locations.copy()
    player_scores = current_game.player_scores.copy()

    # While the target cheese has not yet been eaten by either player
    # We simulate how the game will evolve until that happens
    cheeses = current_game.cheeses
    while target in cheeses:
        # Update the position of all agents
        for player_name, player_position in player_locations.items():
            if player_name == name:
                # Game theory player always moves to target
                action = player_position.choose_action(target, current_game.possible_actions)
            else:
                # Assume Manhattan movements for other players
                action = manh.turn(
                    maze_width=player_position.width,
                    maze_height=player_position.height,
                    name=player_name,
                    player_locations=player_locations,
                    cheese=cheeses,
                    possible_actions=current_game.possible_actions,
                )
            # Update the player location
            player_locations[player_name] = player_position.play_action(
                action=action, possible_actions=current_game.possible_actions
            )
        # Finally update scores players reach a cheese
        cheeses = update_scores(player_locations, player_scores, cheeses)

    return GameInfo(
        player_locations=player_locations,
        player_scores=player_scores,
        cheeses=cheeses,
        possible_actions=current_game.possible_actions,
    )


def best_targets(name, current_game):
    """Recursive function that goes through the trees of possible plays.

    It takes as arguments a given situation, and return a best targets piece of cheese for
    the player, such that aiming to grab these piece of cheese will eventually lead to a
    maximum score.

    Parameters
    ----------
    name : str
        Player name
    current_game : GameInfo
        Current status of the game

    Returns
    -------
    Tuple[List[Location], float]
        Best target and final score
    """

    def _is_game_ended(game_info):
        # The game could be considered as 'completed ' under two conditions:

        if len(game_info.cheeses) == 0:
            # There are no more cheeses
            return True

        # Any player has obtained more than half of the maximum score.
        pscores = game_info.player_scores.values()
        max_score = len(game_info.cheeses) + sum(pscores)
        return any(pscore > 0.5 * max_score for pscore in pscores)

    # First we ask if the current game is over.
    # In that case, there are no target to achieve and the final score is the current one
    best_score_so_far = current_game.player_scores[name]
    best_target_so_far = []
    if _is_game_ended(current_game):
        return best_target_so_far, best_score_so_far

    # If the game has not finished, the player can aim for any of the remaining pieces of cheese.
    # So we will simulate the game to each of the pieces, which will then by recurrence test all
    # the possible trees.
    # It will remember each step as soon as possible, return the complete way to win.
    for target in current_game.cheeses:
        # Play's until go to target
        end_state = simulate_game_until_target(target, name=name, current_game=current_game)
        # Recover the next better movements. Save the moves if are better.
        list_targets, score = best_targets(name=name, current_game=end_state)
        list_targets = [target] + list_targets
        if score > best_score_so_far:
            best_score_so_far = score
            best_target_so_far = list_targets
        elif score == best_score_so_far and len(list_targets) < len(best_target_so_far):
            best_target_so_far = list_targets
    return best_target_so_far, best_score_so_far


@decorator.turn
def turn(maze_width, maze_height, name, player_locations, player_scores, cheese, possible_actions):
    """Return the action that the agent would do, following game theory strategy

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
    player_scores : Dict[str, float]
        Scores for all players in the game.
    cheese : List[int]
        List of available pieces of cheese in the maze.
    possible_actions : List[str]
        List of possible actions.

    Returns
    -------
    str
        The action taken by the program (one of ``possible_actions``).
    """
    current_game = GameInfo(
        player_locations={
            k: Location(v, maze_width, maze_height) for k, v in player_locations.items()
        },
        player_scores=player_scores,
        cheeses=cheese,
        possible_actions=possible_actions,
    )
    targets, _ = best_targets(name, current_game)
    if len(targets) == 0:
        # Nothing to do if there are not targets to achieve
        return possible_actions[0]
    return current_game.player_locations[name].choose_action(targets[0], possible_actions)
