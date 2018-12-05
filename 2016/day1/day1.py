"""
R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3

---
* file to list of moves
* position += move
    * direction => delta
* distance(start, end)

---
N(0, 0) + R4 => E (0, 3)
---

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.

N (0,0) + R2 = E (0,2)
E (0,2) + L3 = N (3,2)
distance = abs(0-3) + abs (0-2) = 3 + 2

---
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.

N (0,0) + R2 = E (0,2)
E (0,2) + R2 = S (0,0)
S (0,0) + R2 = W (-2, 0)

abs(0-2) + 0 = 2
---
* distance(position, position)
* position + position
* rotate(current, direction)
* move(current, )
---
R5, L5, R5, R3 leaves you 12 blocks away.
"""
from collections import namedtuple

RIGHT = 'R'
LEFT = 'L'
NORTH = (0,1)
SOUTH = (0,-1)
EAST = (1,0)
WEST = (-1,0)
ORIENTATION = {
  NORTH: {
    RIGHT: EAST,
    LEFT: WEST,
  },
  SOUTH: {
    'R': WEST,
    'L': EAST
  },

  EAST: {
    'R': SOUTH,
    'L': NORTH,
  },
  WEST: {
    'R': NORTH,
    'L': SOUTH,
  }
}

Position = namedtuple('Position', 'orientation x y')
start = Position(orientation=NORTH, x=0, y=0)

def distance(start, end):
    return (
        abs(start.x - end.x) +
        abs(start.y - end.y)
    )

def add(current, direction):
    x = current.x + direction[0]
    y = current.y + direction[1]
    return (x,y)

def move(current, direction, blocks):
    delta = ORIENTATION[current.orientation][direction]
    print(delta, blocks)
    for _ in range(blocks):
        change = add(current, delta)
        current = Position(orientation=delta, x=change[0], y=change[1])
        print(current)
    return current

def trip(start, moves):
    current = start
    for x in moves:
        direction = x[0]
        blocks = int(x[1:])
        current = move(current, direction, blocks)
    return current

if __name__ == '__main__':
    import sys
    import io

    input_file = sys.argv[1]
    with io.open(input_file) as trip_data:
        moves = [x.strip() for x in trip_data.read().split(',')]
        print(moves)

    end = trip(start, moves)
    print(distance(start, end))
