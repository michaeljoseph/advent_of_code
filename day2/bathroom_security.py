"""

The document goes on to explain that each button to be pressed can be found by

- starting on the previous button
    and moving to adjacent buttons on the keypad:
     U moves up, D moves down, L moves left, and R moves right.

 Each line of instructions corresponds to one button,
 starting at the previous button
 (or, for the first line, the "5" button);

 press whatever button you're on at the end of each line.
 If a move doesn't lead to a button, ignore it.


KEYPAD
1 2 3
4 5 6
7 8 9

ULL
RRDDD
LURDL
UUUUD

You start at "5" and move up (to "2"), [initial position + keypad direction]
left (to "1"), [previous position + keypad direction]
and left (you can't, and stay on "1"), [move doesn't lead to button]
so the first button is 1. [return current position at the end of a line]

Starting from the previous button ("1"), you move right twice (to "3")
[previous line's position == next line's starting position]
and then down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.

Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.

"""

KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

UP = -3
DOWN = 3
LEFT = -1
LEFT_EDGES = [1, 4, 7]
RIGHT = 1
RIGHT_EDGES = [3, 6, 9]


def decode_move(direction, start=5):
    if direction == 'L':
        return start + LEFT if start not in LEFT_EDGES else start
    elif direction == 'R':
        return start + RIGHT if start not in RIGHT_EDGES else start
    elif direction == 'U':
        return start + UP if start + UP > 0 else start
    elif direction == 'D':
        return start + DOWN if start + DOWN < 10 else start


def decode(instructions):
    code = []

    current_number = 5
    for directions in instructions:
        for direction in directions:
            current_number = decode_move(direction, start=current_number)
        code.append(current_number)

    return int(''.join([str(c) for c in code]))
