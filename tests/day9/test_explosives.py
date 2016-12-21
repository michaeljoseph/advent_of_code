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
def test_single_marker(compressed, decompressed, length):
    decompressed_data = decompress(compressed)
    assert decompressed_data == decompressed
    assert len(decompressed_data) == length
