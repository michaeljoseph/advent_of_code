"""
abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, 
    4 of them contain [a letter which appears exactly twice]
    and 3 of them contain [a letter which appears exactly three times].

    Multiplying these together produces a checksum of 
        4 * 3 = 12.
"""

from . import any_repeats, checksum
import pytest


@pytest.mark.parametrize('box_id, repeated, expected', [
    ('abcdef', 2, False),
    ('abcdef', 3, False),

    ('bababc', 2, True),
    ('bababc', 3, True),

    ('abbcde', 2, True),
    ('abbcde', 3, False),

    ('abcccd', 2, False),
    ('abcccd', 3, True),

    ('aabcdd', 2, True),

    ('abcdee', 2, True),

    ('ababab', 3, True),
])
def test_repeats(box_id, repeated, expected):
    assert any_repeats(box_id, repeated) == expected

BOX_IDS = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]
def test_repeat_count():
    assert sum([
        any_repeats(box_id, 2)
        for box_id in BOX_IDS
    ]) == 4
    assert sum([
        any_repeats(box_id, 3)
        for box_id in BOX_IDS
    ]) == 3

def test_checksum():
    assert checksum(BOX_IDS) == 12