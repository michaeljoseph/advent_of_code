from day2.bathroom_security import decode


def test_decode():
    instructions = [
        'ULL'
        'RRDDD'
        'LURDL'
        'UUUUD'
    ]

    assert decode(instructions) == '1985'
