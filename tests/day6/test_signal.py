import pytest

from day6.signal import *

example_input = [
    'eedadn',
    'drvtee',
    'eandsr',
    'raavrd',
    'atevrs',
    'tsrnev',
    'sdttsa',
    'rasrtv',
    'nssdts',
    'ntnada',
    'svetve',
    'tesnvt',
    'vntsnd',
    'vrdear',
    'dvrsen',
    'enarar',
]


def test_extract_column():
    assert (
        extract_column(example_input, 0) ==
        'ederatsrnnstvvde'
    )


def test_transpose_data():
    assert (
        transpose_data(['abc', 'def']) ==
        ['ad', 'be', 'cf']
    )


def test_error_correct_character():
    assert(
        error_correct_character('ederatsrnnstvvde') ==
        'e'
    )


def test_error_correct_data():
    assert(
        error_correct_data(example_input) ==
        'easter'
    )
