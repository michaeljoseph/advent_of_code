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


def is_abba(sequence):
    if not len(sequence) == 4:
        return False

    first_half = sequence[:2]
    different_chars = first_half[0] != first_half[1]
    second_half = sequence[2:]

    return different_chars and first_half == second_half[::-1]
