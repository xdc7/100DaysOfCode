"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""



def count_upper_lower_characters(txt):
    lower_count = 0
    upper_count = 0
    for char in txt:
        if char and char.isalpha():
            if char.islower():
                lower_count += 1
            elif char.isupper():
                upper_count += 1
            else:
                pass
    return (lower_count, upper_count)

entry = input()


print ("\nLOWER CASE: %s \nUPPER CASE: %s" % (count_upper_lower_characters(entry)))