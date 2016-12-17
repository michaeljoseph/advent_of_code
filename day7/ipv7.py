"""
An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.

An ABBA is any four-character sequence which consists of
a pair of two different characters
followed by the reverse of that pair,
such as xyyx or abba.

However, the IP also must
not have an ABBA within any hypernet sequences,
which are contained by square brackets.
"""
import re


def is_abba(sequence):
    if not len(sequence) == 4:
        return False

    first_half = sequence[:2]
    different_chars = first_half[0] != first_half[1]
    second_half = sequence[2:]

    return different_chars and first_half == second_half[::-1]


def contains_abba(sequence):
    x = 0

    while (x+4) <= len(sequence):
        candidate = sequence[x:x+4]
        if is_abba(candidate):
            return True
        x += 1

    return False


def parse_address(address):
    matches = re.match(r'(.*)\[(.*)\](.*)', address).groups()

    return [
        [matches[0], matches[2]],
        matches[1],
    ]


def supports_tls(address):
    address_parts, hypertext = parse_address(address)

    hypertext_contains_abba = contains_abba(hypertext)
    if hypertext_contains_abba:
        return False

    for address_part in address_parts:
        if contains_abba(address_part):
            return True

    return False
