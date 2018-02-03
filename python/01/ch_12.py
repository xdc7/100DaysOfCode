"""Write a function that takes a number and returns the sum of its digits. Raise exception if argument of the wrong type was passed"""

def sum_the_input(num_string):
    count = 0
    for letter in num_string:
        try:
            num = int(letter)
        except ValueError as  ve:
            # print ("Invalid input! Exception: %s" % ve.__str__)
            raise ValueError("Invalid input: ValueError")
            # return None
        except NameError as ne:
            print ("Invalid input! Exception: %s" % ne.__str__)
            return None
        except SyntaxError as  se:
            print ("Invalid input! Exception: %s" % se.__str__)
            return None
        count += num
    return count



# while True:
#     try:
#         print ("Enter some positive numbers without any spaces and hit Enter. For example, 122233 or 2932139 or 21343434")
#         user_input = str(input())
#         if user_input:
#             break
#     except ValueError:
#         print ("Invalid input! Please try again")
#     except NameError:
#         print ("Invalid input! Please try again")
#     except SyntaxError:
#         print ("Invalid input! Please try again")

# print (sum_the_input('123123213'))
print (sum_the_input('000001233344'))
# print (sum_the_input('a'))
# print (sum_the_input('asd3'))
# print (sum_the_input('0'))
# print (sum_the_input())
