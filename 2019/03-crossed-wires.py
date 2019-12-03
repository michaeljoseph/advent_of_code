import attr
import logging
from typing import List, Set
import pytest
from common import get_puzzle

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
log = logging.getLogger(__name__)


@attr.s(auto_attribs=True, frozen=True)
class Point:
    x: int
    y: int
p = Point


def move(start: Point, moves: List[str]) -> Set[Point]:
    locations = set()

    current = start
    log.debug(f'==> {current}')

    for m in moves.split(','):
        direction = m[0]
        magnitude = int(m[1:]) + 1

        if direction == 'R':
            moved_locations = [Point(current.x + i, current.y) for i in range(magnitude)]
        elif direction == 'L':
            moved_locations = [Point(current.x - i, current.y) for i in range(magnitude)]
        elif direction == 'U':
            moved_locations = [Point(current.x, current.y + i) for i in range(magnitude)]
        elif direction == 'D':
            moved_locations = [Point(current.x, current.y - i) for i in range(magnitude)]

        current = moved_locations[-1]

        log.debug(moved_locations)
        locations.update(moved_locations)

    log.debug(f'<== {current}')
    return locations


def distance(a, b):
    log.debug(a)
    log.debug(b)
    return abs(a.x - b.x) + abs(a.y - b.y)


def distance_to_closest_intersection(wire1: str, wire2: str):
    start = p(0, 0)

    l1 = move(start, wire1)
    l2 = move(start, wire2)

    distances = [
        distance(start, location)
        for location in l1.intersection(l2)
    ]

    return min([d for d in distances if d])


def test_point():
    assert move(p(0, 0), 'R2') == set([p(0, 0), p(1, 0), p(2, 0)])


def test_intersection():
    a = set([p(0, 0), p(1, 0), p(2, 0)])
    b = set([p(0, 0), p(0, 1), p(0, 2)])
    assert a.intersection(b) == set([p(0, 0)])


def test_distance():
    assert distance(p(0, 0), p(3, 3)) == 6


@pytest.mark.parametrize('wire1, wire2, distance', [
    (
        'R8,U5,L5,D3',
        'U7,R6,D4,L4',
        6
    ),
    (
        'R75,D30,R83,U83,L12,D49,R71,U7,L72',
        'U62,R66,U55,R34,D71,R55,D58,R83',
        159
    ),
    (
        'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
        135
    )
])
def test_distance_to_closest_intersection(wire1, wire2, distance: int):
    assert distance_to_closest_intersection(wire1, wire2) == distance


if __name__ == '__main__':
    wire1, wire2 = [i for i in get_puzzle(3).split('\n') if i]
    print(distance_to_closest_intersection(wire1, wire2))


