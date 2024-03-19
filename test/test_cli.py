import sys
import subprocess


def dict_to_args(dict_args):
    args = []
    for k, v in dict_args.items():
        args.extend((f"--{k}", *(v if isinstance(v, (list, tuple)) else [str(v)])))
    return args


def test_cli(random_ai):
    # Run a single game with fixed seed.
    args = {
        "random_seed": 2,
        "maze_width": 1,
        "maze_height": 2,
        "mud_percentage": 0.0,
        "nb_cheese": 1,
        "cell_percentage": 100.0,
        "wall_percentage": 0.0,
        "preprocessing_time": 0.0,
        "turn_time": 0.0,
        "render_mode": "no_rendering",
        "players": (random_ai, random_ai),
    }

    process = subprocess.run(
        [sys.executable, "-m", "src.cli"] + dict_to_args(args),
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    if process.returncode != 0:
        main_error = str(subprocess.CalledProcessError(process.returncode, sys.executable))
        raise RuntimeError(main_error + f"\nReason: {process.stderr.decode()}")
