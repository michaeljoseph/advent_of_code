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

from . import any_repeats, checksum, difference, letters_in_common, find_box_ids_with_difference
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

checksum_box_ids = [
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
        for box_id in checksum_box_ids
    ]) == 4
    assert sum([
        any_repeats(box_id, 3)
        for box_id in checksum_box_ids
    ]) == 3

def test_checksum():
    assert checksum(checksum_box_ids) == 12

similar_box_ids = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]
def test_something():
    """
    Confident that your list of box IDs is complete,
    you're ready to find the boxes full of prototype fabric.

    The boxes will have IDs which 
    [differ by exactly one character at the same position in both strings]

    The IDs abcde and axcye are close,
    but they differ by two characters (the second and fourth).
    
    However, the IDs fghij and fguij differ by exactly one character,
    the third (h and u). Those must be the correct boxes.

    What letters are common between the two correct box IDs?
    (In the example above, this is found by removing the differing character
    from either ID, producing fgij.)
    """
    assert difference('abcde', 'axcye') == 2
    assert difference('fghij', 'fguij') == 1
    assert letters_in_common('fghij', 'fguij') == 'fgij'

    assert (
        find_box_ids_with_difference(
            similar_box_ids, 1
        ) 
        == 
        ('fghij', 'fguij')
    )
    assert (
        letters_in_common(
            *find_box_ids_with_difference(similar_box_ids, 1)
        )
        ==
        'fgij'
    )