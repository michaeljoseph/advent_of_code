from itertools import permutations

import pytest

from common import get_puzzle, configure_logging
from intcode import thermal_environment_supervision_terminal

log = configure_logging(__name__)


def amplifier_controller(program, phase_settings, number_of_amplifiers=5, input_value=0):
    last_output = input_value
    for amp in range(number_of_amplifiers):
        inputs = [phase_settings[amp], last_output]
        last_output = thermal_environment_supervision_terminal(program[::], inputs=inputs)

    return last_output


def find_highest_thruster_signal(program):
    # thruster_signals = {
    #     phase_settings: amplifier_controller(program, list(phase_settings))
    #     for phase_settings in permutations([0, 1, 2, 3, 4], 5)
    # }
    return max([
        amplifier_controller(program, list(phase_settings))
        for phase_settings in permutations([0, 1, 2, 3, 4], 5)
    ])


@pytest.mark.parametrize('program, phase_settings, max_thruster_signal', [
    ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0], 43210),
    ([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0], [0, 1, 2, 3, 4], 54321),
    ([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2], 65210),
])
def test_maximum_thruster_signal(program, phase_settings, max_thruster_signal):
    assert amplifier_controller(program, phase_settings) == max_thruster_signal

    assert find_highest_thruster_signal(program) == max_thruster_signal


if __name__ == '__main__':
    acs = [int(x) for x in get_puzzle(7).split(',')]
    print(find_highest_thruster_signal(acs))