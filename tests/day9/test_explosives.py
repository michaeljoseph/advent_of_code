from day9.explosives import *
import pytest


def test_decompress_no_markers():
    assert decompress('ADVENT') == 'ADVENT'


def test_extract_marker():
    assert extract_marker('A(1x5)BC', 0) == ('1x5', 5)


def test_parse_marker():
    assert parse_marker('1x5') == [1, 5]


@pytest.mark.parametrize('compressed, decompressed, length', [
    ('ADVENT', 'ADVENT', 6),
    ('A(1x5)BC', 'ABBBBBC', 7),
    ('(3x3)XYZ', 'XYZXYZXYZ', 9),
    ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG', 11),
    ('(6x1)(1x3)A', '(1x3)A', 6),
    ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY', 18),
])
def test_decompress(compressed, decompressed, length):
    decompressed_data = decompress(compressed)
    assert decompressed_data == decompressed
    assert len(decompressed_data) == length


@pytest.mark.parametrize('compressed, length', [
    ('(3x3)XYZ', 9),
    ('X(8x2)(3x3)ABCY', len('XABCABCABCABCABCABCY')),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
])
def test_v2_decompress_length(compressed, length):
    decompressed_data = decompress(compressed, markers=True)
    assert len(decompressed_data) == length


@pytest.mark.parametrize('compressed, length', [
    ('(3x3)XYZ', 9),
    ('X(8x2)(3x3)ABCY', len('XABCABCABCABCABCABCY')),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
])
def test_decompress_length(compressed, length):
    decompressed_len = decompress_length(compressed)
    assert decompressed_len == length
