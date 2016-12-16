"""
checksum is
the five most common letters in the encrypted name
in order,
with ties broken by alphabetization
"""

import re
from collections import Counter


def parse_room(room):
    room_parts = room.split('-')
    encrypted_name = ''.join(room_parts[:-1])
    sector_id, checksum = re.match(r'(\d*)\[(.*)\]', room_parts[-1:][0]).groups()
    return encrypted_name, sector_id, checksum


def calculate_checksum(encrypted_name):
    c = Counter(encrypted_name)
    return ''.join(sorted([count[0] for count in c.most_common(5)]))

