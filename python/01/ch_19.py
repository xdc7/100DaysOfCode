"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""


def make_even_list(ls):
    # return [ item if i  % 2 == 0 else None for i, item in enumerate(ls)] #Using else doesn't work properly because we have a 'None' element in the list
    return [ item for i, item in enumerate(ls) if i  % 2 == 0] # The 'if' only form works best here

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (make_even_list(a))
