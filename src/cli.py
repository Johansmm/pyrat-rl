import pyrat

from .pyrat_args import parser
from .load_programs import load_players


def launch_game_in_pyrat(players, **kwargs):
    game = pyrat.PyRat(players, **kwargs)
    stats = game.start()

    # Limit turn_durations to 10 values
    for _, player in stats["players"].items():
        num_turns = len(player["turn_durations"])
        player["turn_durations"] = player["turn_durations"][:10]
        if num_turns > 10:
            player["turn_durations"].append("...")

    print(stats)


def main():
    """Command-line interface to run a simple game between two agents"""
    # Include script players in arguments
    parser.add_argument(
        "--players",
        nargs=2,
        required=True,
        help="Modules with agent programs. Each program must follow the format: "
        "<package>.<subpackage>...<program>",
    )
    args = parser.parse_args()

    # Load players
    players = load_players(args.__dict__.pop("players"))

    # Launch game
    launch_game_in_pyrat(players, **vars(args))


if __name__ == "__main__":
    main()
