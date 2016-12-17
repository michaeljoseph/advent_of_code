from day7.ipv7 import *


def test_abba_sequence():
    assert is_abba('xyyx')
    assert is_abba('abba')
    assert not is_abba('xyxyx')
    assert not is_abba('aaaa')


def test_contains_abba():
    assert contains_abba('ioxxoj')
    assert not contains_abba('zxcvbn')

