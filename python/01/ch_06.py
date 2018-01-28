from __future__ import print_function
"""
Say you have a list value like tSay you have a list value like t"Say you have a list value like tSay you have a list value like t"Say you have a list value like tSay you have a list value like t"Say you have a list value like tSay you have a list value like t"Say you have a list value like tSay you have a list value like t"Say you have a list value like tSay you have a list value like t"Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument 
and returns a string with all the items separated by a comma and a space, 
with and inserted before the last item. 
For example, passing the previous spam list to the function would return 
'apples, bananas, tofu, and cats'.
 But your function should be able to work with any list value passed to it.
"""

spam = ['apples', 'bananas', 'tofu', 'cats']
spam= ['apples']
spam = ['']

def list_to_string(ls):
    if len(ls) < 1:
        return
    elif len(ls) == 1:
        return "".join(ls)
    else:
        return(", ".join(ls[:-1]) + ", and " + "".join(ls[-1:]))
    
    
print (list_to_string(spam))



"""
Say you have a list of lists where each value in the inner lists is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

You can think of grid[x][y] as being the character at the x- and y-coordinates of a picture drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

Copy the previous grid value, and write code that uses it to print the image.

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
""" 



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



# Simple solution using nested for loops
# for y in range(len(grid[0])):
#     for x in range(len(grid)-1,-1,-1):
#         print(grid[x][y], end='')
#     print()

# Solution using list comprehension
m = grid
tx = [[row[i] for row in m ]for i in range(len(m[0]))]

for row in tx:
    print (''.join(row))
