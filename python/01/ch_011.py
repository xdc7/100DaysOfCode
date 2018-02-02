"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1 1 2 3 5 8 13)
0 1 2 3 4 5 6 7 8 9 10
"""
      


def gen_fib(num):
    # Handling all the edge cases for 0, 1, and 2
    if num <= 0:
        return 0
    elif num == 1:
        fib_list = [1]
        return fib_list
    elif num == 2:
        fib_list = [1,1]
        return fib_list
    # At this point the user input is greater than 2. Therefore, initialize the fibonacci list with the first 2 values
    fib_list = [1,1]
    # Now iterate over the range of 1 and num-1 (num-1 because we already have 2 members in the list)
    for i in range (1, num - 1):
        # Generate the next number in the fibonacci sequence by adding the last 2 numbers in the list
        fib_list.append(fib_list[i - 1] + fib_list[i])
    return fib_list


while True:
    try:
        print ("How many Fibonnaci numbers do you want to generate? Please enter a valid postive integer")
        user_input = int(input())
        if user_input < 0:
            raise ValueError
        break
    except ValueError:
        print ("Invalid input! Please enter a valid integer")
    except NameError:
        print ("Invalid input! Please enter a valid integer")
    except SyntaxError:
        print ("Invalid input! Please enter a valid integer")        
print (gen_fib(user_input))