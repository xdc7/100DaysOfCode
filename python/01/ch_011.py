"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
0 1 2 3 4 5 6 7 8 9 10
"""

def gen_fib(num):
    num_list = range (num)
    res = 0
    for i in range (len(num_list) + 1 ):
        print ("i=%d and res=%d" %(i,res))
        if i == 0:
            res = 1
            print (res)
        elif i == 1:
            res += 1
            print (res)
            
        else:
            res = res + num_list[i - 1]
            print (res)
            
            


print (gen_fib(7))