import re
from collections import defaultdict, Counter


def parse_room(room):
    room_parts = room.split('-')
    encrypted_name = ''.join(room_parts[:-1])
    sector_id, checksum = re.match(r'(\d*)\[(.*)\]', room_parts[-1:][0]).groups()
    return encrypted_name, sector_id, checksum


def calculate_checksum(encrypted_name):
    c = Counter(encrypted_name)
    occurrence_map = defaultdict(lambda: [])

    for value, occurrences in c.most_common():
        occurrence_map[occurrences].append(value)

    checksum = []
    for occurrence in reversed(sorted(occurrence_map.keys())):
        letters = sorted(occurrence_map[occurrence])
        checksum.append(''.join(letters))

    return ''.join(checksum)[:5]
