from day2.bathroom_security import decode


def test_single_instruction():
    instructions = [
        'U'
    ]

    assert decode(instructions) == '2'
