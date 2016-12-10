"""

The document goes on to explain that each button to be pressed can be found by
 starting on the previous button and moving to adjacent buttons on the keypad:
 U moves up, D moves down, L moves left, and R moves right.

 Each line of instructions corresponds to one button, starting at the previous
 button (or, for the first line, the "5" button);
 press whatever button you're on at the end of each line.
 If a move doesn't lead to a button, ignore it.


KEYPAD
1 2 3
4 5 6
7 8 9


"""


def decode(instructions):
    return '2'
