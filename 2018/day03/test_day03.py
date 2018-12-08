from pprint import pprint 
from . import parse_claim, parse_claims, overlaps, total_overlaps
import pytest


def test_parse_claim():
    assert parse_claim('#1 @ 527,351: 24x10') == (527, 351, 24, 10)


list_of_claims = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
    '#1 @ 527,351: 24x10',
]
expected_claims = [
    (1, 3, 4, 4),
    (3, 1, 4, 4),
    (5, 5, 2, 2),
    (527, 351, 24, 10)
]
def test_parse_claims():
    assert parse_claims(list_of_claims) == expected_claims 


def test_overlaps():
    a, b, c, _ = expected_claims
    assert overlaps(a, b) == 4
    assert overlaps(a, c) == 0
    assert overlaps(b, c) == 0


def test_overlap():
    assert total_overlaps(list_of_claims) == 4