
# The screen is 50 pixels wide and 6 pixels tall, all of which start off

# rect AxB
# rotate row y=A by B
# rotate column x=A by B
import re

RECT = 'rect'


def parse_dimensions(dimensions):
    return re.match(r'(\d*)x(\d*)', dimensions).groups()


def parse_instruction(instruction):
    if instruction.startswith('rect'):
        x, y = parse_dimensions(instruction[5:])
        return RECT, int(x), int(y)

    return False


def parse_instruction_for_pixels(instruction):

    result = parse_instruction(instruction)
    if result:
        op, x, y = result
        return x * y
    return 0


def how_many_pixels_are_lit(instructions):
    pixels = 0
    for instruction in instructions:
        pixels += parse_instruction_for_pixels(instruction)

    return pixels


if __name__ == '__main__':
    import sys, io

    input_file = sys.argv[1]
    instructions = [x.strip() for x in io.open(input_file).readlines()]

    print(how_many_pixels_are_lit(instructions))