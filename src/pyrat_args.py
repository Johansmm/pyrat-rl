__all__ = ["pyrat", "parser"]

import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def suppress_output():
    # Redirect stdout, stderr and exit to temporal objects
    old_stdout, old_stderr, old_exit = sys.stdout, sys.stderr, sys.exit
    sys.stdout, sys.stderr, sys.exit = StringIO(), StringIO(), lambda *args: None
    try:
        yield
    finally:
        # Restore original objects
        sys.stdout, sys.stderr, sys.exit = old_stdout, old_stderr, old_exit


# Import pyrat arguments inside of suppress_output context to support new arguments
with suppress_output():
    import pyrat

    parser = pyrat.parser
