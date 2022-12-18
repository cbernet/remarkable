import os

from remarkable.locate import abspath_root, abspath_data


def test_root():
    root = abspath_root()
    elements = os.listdir(root)
    assert {"remarkable", "tests"}.issubset(elements)


def test_data():
    image = abspath_data("lambdas/lambdas - page 1.png")
    assert image.exists()
