import pytest
from ch_12 import sum_the_input

def test_positive_numbers_01():
    assert sum_the_input('1233344') == 20

def test_positive_numbers_02():
    assert sum_the_input('133243243242342033344') == 59

def test_positive_numbers_03():
    assert sum_the_input('000001233344000001') == 21

def test_zero():
    assert sum_the_input('00000000') == 0

def test_alphanumeric_values_01():
    with pytest.raises(ValueError) as e_info:
        sum_the_input('asd3')

def test_no_arguments():
    with pytest.raises(TypeError) as e_info:
        sum_the_input()

def test_no_input():
    assert sum_the_input('')  == 0

# def test_alphanumeric_values_02():
#     assert sum_the_input('1a') == 20
# def test_no_values():
#     assert sum_the_input('') == 20

# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)




# print (sum_the_input('123123213'))
# print (sum_the_input('a'))
# print (sum_the_input('asd3'))
# print (sum_the_input('0'))
# print (sum_the_input(''))