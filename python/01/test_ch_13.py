import pytest

from ch_13 import calc_upper_lower

def test_empty_string():
    assert calc_upper_lower("") == None

def test_no_arguments():
    with pytest.raises(TypeError) as e_info:
        calc_upper_lower()

def test_valid_sentence():
    assert calc_upper_lower("Hello world!") == "UPPER CASE 1\nLOWER CASE 9"

def test_valid_sentence_02():
    assert calc_upper_lower("Hello, Ronaldo!!!") == "UPPER CASE 2\nLOWER CASE 10"

def test_invalid_sentence_01():
    assert calc_upper_lower("#$$^%$%&@@#$~`!!!") == "UPPER CASE 0\nLOWER CASE 0"

def test_invalid_sentence_02():
    assert calc_upper_lower("3432432432@!#") == "UPPER CASE 0\nLOWER CASE 0"