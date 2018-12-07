from .frequency import calculate_frequency, find_first_duplicate

import pytest


@pytest.mark.parametrize('changes, final_frequency', [
    ('+1, -2, +3, +1', 3),
    ('+1, +1, +1', 3),
    ('+1, +1, -2', 0),
    ('-1, -2, -3', -6),
])
def test_calculate_frequency_examples(changes, final_frequency):
    end_frequency, _ = calculate_frequency(changes.split(','))
    assert end_frequency == final_frequency

@pytest.mark.parametrize('changes, duplicate_frequency', [
    ('+1, -2, +3, +1', 2),
    ('+1, -1', 0),
    ('+3, +3, +4, -2, -4', 10),
    ('-6, +3, +8, +5, -6', 5),
    ('+7, +7, -2, -7, -4', 14),
])
def test_find_first_duplicate_examples(changes, duplicate_frequency):
    assert find_first_duplicate(changes.split(',')) == duplicate_frequency