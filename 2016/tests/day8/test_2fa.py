from day8.twofa import *


def test_parse_dimensions():
    assert parse_dimensions('3x2') == ('3', '2')
    assert parse_dimensions('2x4') == ('2', '4')
    assert parse_dimensions('342x42') == ('342', '42')


def test_parse_instruction_rect():
    assert parse_instruction('rect 3x2') == (RECT, 3, 2)


def test_parse_rotation():
    assert parse_rotation('x=1 by 1') == ('1', '1')


def test_parse_instruction_row():
    assert parse_instruction('rotate column x=1 by 1') == (COLUMN, 1, 1)


def test_initialise_screen():
    assert (
        initialise_screen(2, 2) == [
            ['.', '.'],
            ['.', '.'],
        ]
    )


def test_apply_rect_instruction():
    screen = initialise_screen(2, 2)

    instruction = 'rect 1x1'
    expected_screen = [
        ['#', '.'],
        ['.', '.'],
    ]
    assert apply_instruction(screen, instruction) == expected_screen


def test_apply_rect_large():
    screen = initialise_screen(7, 3)
    instruction = 'rect 3x2'
    expected_screen = [
        ['#', '#', '#', '.', '.', '.', '.'],
        ['#', '#', '#', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
    ]
    assert apply_instruction(screen, instruction) == expected_screen


def test_parse_screen():
    screen = [
        '#.',
        '#.',
        '..',
    ]
    expected_screen = [
        ['#', '.'],
        ['#', '.'],
        ['.', '.'],
    ]
    assert parse_screen(screen) == expected_screen


def test_rotate_column():
    screen = [
        ['#', '.'],
        ['#', '.'],
        ['.', '.'],
    ]
    expected_screen = [
        ['.', '.'],
        ['#', '.'],
        ['#', '.'],
    ]
    assert rotate_column(screen, 0, 1) == expected_screen


def test_rotate_row():
    screen = parse_screen([
        '#.#....',
        '###....',
        '.#.....',
    ])

    expected_screen = parse_screen([
        '....#.#',
        '###....',
        '.#.....',
    ])

    assert rotate_row(screen, 0, 4) == expected_screen


def test_rotate_row_input():
    screen = parse_screen([
        '#.................................................'
    ])
    expected_screen = parse_screen([
        '..#...............................................'
    ])
    assert rotate_row(screen, 0, 2) == expected_screen


def test_apply_rotate_column():
    screen = parse_screen([
        '###....',
        '###....',
        '.......',
    ])
    instruction = 'rotate column x=1 by 1'

    expected_screen = parse_screen([
        '#.#....',
        '###....',
        '.#.....',
    ])

    assert apply_instruction(screen, instruction) == expected_screen


def test_apply_rotate_row():
    screen = parse_screen([
        '#.#....',
        '###....',
        '.#.....',
    ])
    instruction = 'rotate row y=0 by 4'
    expected_screen = parse_screen([
        '....#.#',
        '###....',
        '.#.....',
    ])

    assert apply_instruction(screen, instruction) == expected_screen


def test_apply_instructions():
    screen = initialise_screen(7, 3)

    expected_screen = parse_screen([
        '.#..#.#',
        '#.#....',
        '.#.....',
    ])

    instructions = [
        'rect 3x2',
        'rotate column x=1 by 1',
        'rotate row y=0 by 4',
        'rotate column x=1 by 1',
    ]
    assert apply_instructions(screen, instructions) == expected_screen


def test_parse_instruction_for_pixels():
    assert parse_instruction_for_pixels('rect 4x2') == 8


def test_how_many_pixels_are_lite():
    assert how_many_pixels_are_lit(['rect 3x2']) == 6
