import re
from collections import defaultdict, Counter


def parse_room(room):
    room_parts = room.split('-')
    encrypted_name = '-'.join(room_parts[:-1])
    sector_id, checksum = re.match(r'(\d*)\[(.*)\].*', room_parts[-1:][0]).groups()
    return encrypted_name, int(sector_id), checksum


def rotate_letter(letter, times):
    return 'b'


def decrypt_room_name(room, sector_id):
    return 'very encrypted name'


def calculate_checksum(encrypted_name):
    c = Counter(encrypted_name.replace('-', ''))
    occurrence_map = defaultdict(lambda: [])

    for value, occurrences in c.most_common():
        occurrence_map[occurrences].append(value)

    checksum = []
    for occurrence in reversed(sorted(occurrence_map.keys())):
        letters = sorted(occurrence_map[occurrence])
        checksum.append(''.join(letters))

    return ''.join(checksum)[:5]


def valid_rooms_sector_sum(rooms):
    sector_id_total = 0
    for room in rooms:
        encrypted_name, sector_id, checksum = parse_room(room)
        if checksum == calculate_checksum(encrypted_name):
            sector_id_total += sector_id

    return sector_id_total


if __name__ == '__main__':
    import sys, io

    input_file = sys.argv[1]

    rooms = io.open(input_file).readlines()
    print(valid_rooms_sector_sum(rooms))
