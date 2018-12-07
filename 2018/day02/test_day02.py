from . import repeats, checksum

def test_checksum():
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
    assert repeats('abcdef', 2) == 0 
    assert repeats('abcdef', 3) == 0 

    box_ids = [
    ]
    assert checksum(box_ids) == 12