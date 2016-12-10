import pytest

from day1.day1 import *


@pytest.mark.parametrize('start, end, dist', [
    (
        Position(orientation=NORTH, x=0, y=0),
        Position(orientation=NORTH, x=0, y=0),
        0
    ),
    (
        Position(orientation=NORTH, x=0, y=0),
        Position(orientation=NORTH, x=5, y=2),
        7
    ),
    (
        Position(orientation=NORTH, x=2, y=3),
        Position(orientation=NORTH, x=1, y=5),
        3
    ),
])
def test_distance(start, end, dist):
    assert distance(start, end) == dist

@pytest.mark.parametrize('moves, dist', [
    (['R2', 'L3'], 5),
    (['R5', 'L5', 'R5', 'R3'], 12),
    (['R2', 'R2', 'R2'], 2),
    (['R10'], 10),
])
def test_trip_distance(moves, dist):
    start = Position(orientation=NORTH, x=0, y=0)
    end = trip(start, moves)
    assert distance(start, end) == dist
