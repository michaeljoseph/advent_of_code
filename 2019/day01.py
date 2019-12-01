from pathlib import Path
import sys

import pytest


def fuel(mass):
    """
    find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2.
    """
    return int(int(mass) / 3) - 2


@pytest.mark.parametrize('mass, expected_fuel', [
    ('12', 2),
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583)
])
def test_fuel(mass, expected_fuel):
    assert fuel(mass) == expected_fuel


if __name__ == '__main__':

    len(sys.argv) < 2 and sys.exit(f'{sys.argv[0]} <path to input file>')

    puzzle_input = Path(sys.argv[1])
    not puzzle_input.exists() and sys.exit(f'{puzzle_input} not found')

    print(sum([
        fuel(mass.strip())
        for mass in puzzle_input.read_text().split('\n')
        if mass
    ]))
