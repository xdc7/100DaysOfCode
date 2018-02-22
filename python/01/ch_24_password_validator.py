"""You know these Create a new password forms? They do a lot of checks to make sure you make a password that is hard to guess and you will surely forget.

In this Bite you will write a validator for such a form field.

Complete the validate_password function below. It takes a password str and validates that it:

is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
If the password matches all criteria the function should store the password in used_passwords and return True.

Have fun, keep calm and code in Python!"""

import re
def validate_password(password):
    used_passwords = []
    length_re = re.compile(r'.{8,}')
    uppercase_re = re.compile(r'.*[A-Z]')
    lowercase_re = re.compile(r'.*[a-z].*[a-z]')
    number_re = re.compile(r'.*\d.*\d')
    punctuation_re = re.compile(r'[\!\@\#\$\%\&]')

    if (length_re.search(password) is not None
        and uppercase_re.search(password) is not None
        and lowercase_re.search(password) is not None
        and number_re.search(password) is not None
        and punctuation_re.search(password) is not None
        and password not in used_passwords):
        used_passwords.append(password)
        return True
    else:
        return False

print (validate_password("a4a4Aa3!@#$%&"))