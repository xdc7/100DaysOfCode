"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3"""

def centered_average(int_list):
    if len(int_list) < 3:
        return None
    smallest = min(int_list)
    largest = max(int_list)
    smallest_found = False
    largest_found = False
    counter = 0
    total = 0
    for num in int_list:
        if num == smallest and not smallest_found:
            smallest_found = True
            continue
        elif num == largest and not largest_found:
            largest_found = True
            continue
        counter += 1
        total += num
    return (total // counter)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))


