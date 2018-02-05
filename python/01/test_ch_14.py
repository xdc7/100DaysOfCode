import pytest

from ch_14 import sum67

# print(sum67([1, 2, 2]))
# print(sum67([1, 2, 2, 6, 99, 99, 7]))
# print(sum67([1, 1, 6, 7, 2]))
# print(sum67([1, 1, 6, 7, 2]))
# print(sum67([6, 1,  7]))
# print(sum67([6, 1,  7, 1, 2]))
# print(sum67([1, 1,  0, 6, 7]))
# print(sum67([1, 1,  0, 6, 7, 1, 7]))

def test_empty_string():
    assert sum67("") == "Not a list"

def test_no_arguments():
    with pytest.raises(TypeError) as e_info:
        sum67()

def test_valid_number_list():
    assert sum67([1, 2, 2]) == 5

def test_valid_number_list_02():
    assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5

def test_valid_number_list_03():
    assert sum67([1, 1, 6, 7, 2]) == 4

def test_valid_number_list_04():
    assert sum67([6, 1,  7, 1, 2]) == 3

def test_valid_number_list_05():
    assert sum67([1, 1,  0, 6, 7]) == 2

def test_valid_number_list_06():
    assert sum67([1, 1,  0, 6, 7]) == 2

def test_valid_number_list_07():
    assert sum67([1, 2, 2]) == 5

def test_valid_number_list_08():
    assert sum67([1, 1,  0, 6, 7, 1, 7]) == 10

def test_valid_number_list_09():
    assert sum67([0]) == 0


def test_invalid_number_list_01():
    assert sum67(['a','c','f']) == "Invalid item. Only numbers accepted"

def test_invalid_number_list_02():
    assert sum67("3432432432@!#") == "Not a list"