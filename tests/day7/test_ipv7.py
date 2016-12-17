from day7.ipv7 import *


def test_abba_sequence():
    assert is_abba('xyyx')
    assert is_abba('abba')
    assert not is_abba('xyxyx')
    assert not is_abba('aaaa')


def test_contains_abba():
    assert contains_abba('ioxxoj')
    assert not contains_abba('zxcvbn')


@pytest.mark.parametrize('ip_address, address_parts', [
    ('abba[mnop]qrst', [['abba', 'qrst'], 'mnop']),
    ('ioxxoj[asdfgh]zxcvbn', [['ioxxoj', 'zxcvbn'], 'asdfgh']),
    ('abcd[bddb]xyyx', [['abcd', 'xyyx'], 'bddb']),
    ('aaaa[qwer]tyui', [['aaaa', 'tyui'], 'qwer']),
])
def test_parse_address(ip_address, address_parts):
    assert parse_address(ip_address) == address_parts
