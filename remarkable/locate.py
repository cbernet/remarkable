import pathlib
import remarkable


def abspath_root():
    return pathlib.Path(remarkable.__file__).parents[1]


def abspath_data(path):
    return abspath_root() / f"tests/data/{path}"
