import re
from copy import deepcopy

RECT = 'rect'
COLUMN = 'rotate column'
ROW = 'rotate row'
SCREEN = (50, 6)


def parse_dimensions(dimensions):
    return re.match(r'(\d*)x(\d*)', dimensions).groups()


def parse_rotation(rotation):
    return re.match(r'.*=(\d*) by (\d*)', rotation).groups()


def parse_instruction(instruction):
    if instruction.startswith(RECT):
        x, y = parse_dimensions(instruction[5:])
        return RECT, int(x), int(y)

    elif instruction.startswith(COLUMN):
        column, increment = parse_rotation(instruction[len(COLUMN)+1:])
        return COLUMN, int(column), int(increment)
    elif instruction.startswith(ROW):
        row, increment = parse_rotation(instruction[len(ROW)+1:])
        return ROW, int(row), int(increment)

    return False


def initialise_screen(columns, rows):
    screen = []

    for y in range(rows):
        screen.append(['.'] * columns)

    return screen


def parse_screen(data):
    screen = []
    for line in data:
        screen.append([x for x in line])
    return screen


def rotate_column(data, column, increment):
    tmp_data = deepcopy(data)

    for row_idx, row in enumerate(data):
        target_row_index = row_idx - increment
        if target_row_index < 0:
            target_row_index += len(data)

        data[row_idx][column] = tmp_data[target_row_index][column]

    return data


def rotate_row(data, row, increment):
    tmp_data = deepcopy(data)

    for col_idx, col in enumerate(data[row]):
        new_idx = col_idx - increment
        if new_idx < 0:
            new_idx += len(data[row])
        data[row][col_idx] = tmp_data[row][new_idx]

    return data


def apply_instruction(screen, instruction):
    op, x, y = parse_instruction(instruction)

    if op == RECT:
        for i in range(x):
            for j in range(y):
                screen[j][i] = '#'

    elif op == COLUMN:
        column, increment = x, y
        screen = rotate_column(screen, column, increment)

    elif op == ROW:
        row, increment = x, y
        screen = rotate_row(screen, row, increment)

    return screen


def apply_instructions(screen, instructions):
    for instruction in instructions:
        screen = apply_instruction(screen, instruction)

    return screen


def print_screen(screen):
    for line in screen:
        print(''.join(line))


def parse_instruction_for_pixels(instruction):
    result = parse_instruction(instruction)
    if result:
        op, x, y = result
        if op == RECT:
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

    print('{} pixels are lit'.format(how_many_pixels_are_lit(instructions)))

    screen = initialise_screen(SCREEN[0], SCREEN[1])

    screen = apply_instructions(screen, instructions)

    # ZJHRKCPLYJ
    print_screen(screen)
