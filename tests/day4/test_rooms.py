import pytest
from day4.rooms import *


def test_parse_room():
    room = 'aaaaa-bbb-z-y-x-123[abxyz]'
    encrypted_name, sector_id, checksum = parse_room(room)

    assert encrypted_name == 'aaaaa-bbb-z-y-x'
    assert sector_id == 123
    assert checksum == 'abxyz'


@pytest.mark.parametrize('encrypted_name, checksum', [
    ('aaaaa-bbb-z-y-x', 'abxyz'),
    ('a-b-c-d-e-f-g-h', 'abcde'),
    ('not-a-real-room', 'oarel'),
])
def test_checksum(encrypted_name, checksum):
    assert calculate_checksum(encrypted_name) == checksum


@pytest.mark.parametrize('encrypted_name, checksum', [
    ('totally-real-room', 'decoy'),
])
def test_bad_checksum(encrypted_name, checksum):
    assert not calculate_checksum(encrypted_name) == checksum


def test_sector_sum():
    rooms = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
    ]
    assert 1514 == valid_rooms_sector_sum(rooms)


@pytest.mark.parametrize('letter, rotations, rotated_letter', [
    ('a', 1, 'b'),
    ('b', 2, 'd'),
    ('z', 1, 'a'),
    ('z', 0, 'z'),
])
def test_rotate_letter(letter, rotations, rotated_letter):
    assert rotate_letter(letter, rotations) == rotated_letter


def test_decrypt_room_name():
    encrypted_name = 'qzmt-zixmtkozy-ivhz-343'
    sector_id = 343
    assert decrypt_room_name(encrypted_name, sector_id) == 'very encrypted name'
