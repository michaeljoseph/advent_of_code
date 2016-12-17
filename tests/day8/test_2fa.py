from day8.twofa import *


def test_parse_dimensions():
    assert parse_dimensions('3x2') == ('3', '2')
    assert parse_dimensions('2x4') == ('2', '4')
    assert parse_dimensions('342x42') == ('342', '42')


def test_parse_instruction():
    assert parse_instruction('rect 3x2') == (RECT, 3, 2)


def test_parse_instruction_for_pixels():
    assert parse_instruction_for_pixels('rect 4x2') == 8


def test_how_many_pixels_are_lite():
    assert how_many_pixels_are_lit(['rect 3x2']) == 6