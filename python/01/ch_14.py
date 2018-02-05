"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4"""

def sum67(list_of_numbers):
    total = 0
    count_flag = True
    six_found = False
    seven_found = False
    if not isinstance(list_of_numbers, list):
        return "Not a list"
    for num in list_of_numbers:
        if not isinstance(num,int):
            return "Invalid item. Only numbers accepted"
        if num == 6:
            six_found = True
            count_flag = False
            # continue
        elif num == 7:
            if six_found:
                seven_found = True
                count_flag = True
                six_found = False
                continue
            # continue
        if count_flag and six_found == False :
            total += num
    return total


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([6, 1,  7]))
print(sum67([6, 1,  7, 1, 2]))
print(sum67([1, 1,  0, 6, 7]))
print(sum67([1, 1,  0, 6, 7, 1, 7]))
print(sum67([0]))
print(sum67(["a","b","c",1,2,3]))
print(sum67([1,2,"a","b","c",1,2,3]))
