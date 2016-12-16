import pytest
from day4.rooms import parse_room, calculate_checksum


def test_parse_room():
    room = 'aaaaa-bbb-z-y-x-123[abxyz]'
    encrypted_name, sector_id, checksum = parse_room(room)

    assert encrypted_name == 'aaaaabbbzyx'
    assert sector_id == '123'
    assert checksum == 'abxyz'


@pytest.mark.parametrize('encrypted_name, checksum', [
    ('aaaaabbbzyx', 'abxyz'),
    ('abcdefgh', 'abcde'),
    ('notarealroom', 'oarel'),
])
def test_checksum(encrypted_name, checksum):
    assert calculate_checksum(encrypted_name) == checksum


@pytest.mark.parametrize('encrypted_name, checksum', [
    ('totallyrealroom', 'decoy'),
])
def test_bad_checksum(encrypted_name, checksum):
    assert not calculate_checksum(encrypted_name) == checksum
