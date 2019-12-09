import pytest

from common import get_puzzle, configure_logging
from intcode import thermal_environment_supervision_terminal, int_code_v5


@pytest.mark.parametrize('program, expected_output', [
    ([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]),
    ([1102,34915192,34915192,7,4,7,99,0], [1219070632396864]),
    ([104,1125899906842624,99], [1125899906842624])
])
def test_boost(program, expected_output):
    memory, outputs = int_code_v5(program, [])
    assert expected_output == outputs


if __name__ == '__main__':
    boost = [int(x) for x in get_puzzle(9).split(',')]
    print(boost)
