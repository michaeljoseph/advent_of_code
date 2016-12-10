import pytest

from day2.bathroom_security import *


def test_single_instruction():
    instructions = [
        'ULL',
        'RRDDD',
        'LURDL',
        'UUUUD',
    ]
    assert decode(instructions) == 1985


@pytest.mark.parametrize('start, expected', [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1),
    (5, 2),
    (6, 3),
    (7, 4),
    (8, 5),
    (9, 6),
])
def test_up(start, expected):
    assert decode_move('U', start=start) == expected


@pytest.mark.parametrize('start, expected', [
    (1, 4),
    (2, 5),
    (3, 6),
    (4, 7),
    (5, 8),
    (6, 9),
    (7, 7),
    (8, 8),
    (9, 9),
])
def test_down(start, expected):
    assert decode_move('D', start=start) == expected


@pytest.mark.parametrize('start, expected', [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 4),
    (6, 5),
    (7, 7),
    (8, 7),
    (9, 8),
])
def test_left(start, expected):
    assert decode_move('L', start=start) == expected


@pytest.mark.parametrize('start, expected', [
    (1, 2),
    (2, 3),
    (3, 3),
    (4, 5),
    (5, 6),
    (6, 6),
    (7, 8),
    (8, 9),
    (9, 9),
])
def test_right(start, expected):
    assert decode_move('R', start=start) == expected

