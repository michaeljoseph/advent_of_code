from pathlib import Path
import sys

import pytest
import requests
import browser_cookie3


def run_program(program):
    opcodes = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }

    idx = 0
    done = False
    while not done:
        parameters = program[idx:idx + 4]
        done = parameters[0] == 99
        if done:
            break

        opcode, input1, input2, output = parameters
        operation = opcodes.get(opcode)
        if not operation:
            raise Exception(f'Something went wrong, unknown opcode {opcode}')

        program[output] = opcodes[opcode](program[input1], program[input2])
        idx += 4

    return program


def compute(program, noun, verb):
    return run_program([program[0], noun, verb] + program[3:])[0]


@pytest.mark.parametrize('input, output', [
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
])
def test_opcode(input, output):
    assert run_program(input) == output


def test_compute():
    program = [int(x) for x in Path(f'day2_input.txt').read_text().split(',')]
    assert compute(program, 12, 2) == 3101878
    assert compute(program, 84, 44) == 19690720


if __name__ == '__main__':
    puzzle_input = Path(sys.argv[1]) if len(sys.argv) > 1 and Path(sys.argv[1]).exists() else None

    if not puzzle_input:
        AOC = 'https://adventofcode.com'
        session = requests.Session()
        session.cookies = browser_cookie3.load()

        day = 2
        puzzle_input = Path(f'day{day}_input.txt')

        if not puzzle_input.exists():
            print(f'Downloading day {day} puzzle input')
            puzzle_input.write_text(session.get(f'{AOC}/2019/day/{day}/input').text)

    gravity_assist_program = [int(x) for x in puzzle_input.read_text().split(',')]

    print('12,2 =', compute(gravity_assist_program, 12, 2))

    answer = 19690720
    noun, verb = [
        (noun, verb)
        for noun in range(100)
        for verb in range(100)
        if compute(gravity_assist_program, noun, verb) == answer
    ][0]

    # 👀 100 * noun + verb
    print(f'{noun},{verb} =', compute(gravity_assist_program, noun, verb))
    print(f'100 * {noun} + {verb} =', (100 * noun) + verb)
