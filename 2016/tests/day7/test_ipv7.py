import pytest

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
    ('abba[mnop]qrst', [['abba', 'qrst'], ['mnop']]),
    ('ioxxoj[asdfgh]zxcvbn', [['ioxxoj', 'zxcvbn'], ['asdfgh']]),
    ('abcd[bddb]xyyx', [['abcd', 'xyyx'], ['bddb']]),
    ('aaaa[qwer]tyui', [['aaaa', 'tyui'], ['qwer']]),
])
def test_parse_address(ip_address, address_parts):
    assert parse_address(ip_address) == address_parts


def test_parse_address_multiple_hypertext():
    ip_address = 'gdlrknrmexvaypu[crqappbbcaplkkzb]vhvkjyadjsryysvj[nbvypeadikilcwg]jwxlimrgakadpxu[dgoanojvdvwfabtt]yqsalmulblolkgsheo'
    address_parts = [
        ['gdlrknrmexvaypu', 'vhvkjyadjsryysvj', 'jwxlimrgakadpxu', 'yqsalmulblolkgsheo'],
        ['crqappbbcaplkkzb', 'nbvypeadikilcwg', 'dgoanojvdvwfabtt'],
    ]
    assert parse_address(ip_address) == address_parts


@pytest.mark.parametrize('ip_address, tls', [
    ['abba[mnop]qrst', True],
    ['ioxxoj[asdfgh]zxcvbn', True],
    ['abcd[bddb]xyyx', False],
    ['aaaa[qwer]tyui', False],
])
def test_supports_tls(ip_address, tls):
    assert supports_tls(ip_address) == tls


def test_count_supported_tls_addresses():
    addresses = [
        'abba[mnop]qrst',
        'ioxxoj[asdfgh]zxcvbn',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
    ]
    assert count_supported_tls_addresses(addresses) == 2