import os
import sys
import pytest

program = b"""
import random

def turn(*args):
    # Taken one action different to 'nothing'
    actions = ['north', 'east', 'south', 'west']
    return random.choice(actions)
"""


def from_path_to_program(path):
    # A program must follow the format <package>.<subpackage>...<program>
    program = os.path.splitext(str(path))[0].replace(os.sep, '.')
    if program.startswith('C:.'):
        # Remove 'C:' in windows
        program = program[3:]
    return program


@pytest.fixture(scope="session")
def random_ai(tmp_path_factory):
    program_path = tmp_path_factory.mktemp("programs") / "random_ai.py"
    with open(program_path, "wb") as f:
        f.write(program)

    # Include base directory in python path, enabling to recognize program by importlib/cli
    os.environ["PYTHONPATH"] = program_path.parts[0]
    sys.path.append(program_path.parts[0])
    return from_path_to_program(program_path)
