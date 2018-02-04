"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

def calc_upper_lower(sentence):
    count_upper = 0
    count_lower = 0
    if not sentence:
        return None
    for char in sentence:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    result = "UPPER CASE {0}\nLOWER CASE {1}".format(count_upper, count_lower)
    return result