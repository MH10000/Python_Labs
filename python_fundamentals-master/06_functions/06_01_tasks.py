'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def func_div_one(x):
    return x % 4 == 0 or x % 7 == 0

def func_div_two(y):
    return y % 4 == 0 and y % 7 == 0

user_input = int(input("Enter a number between 1 and 1,000,000,000: "))

func_1 = func_div_one(user_input)
func_2 = func_div_two(user_input)

print(func_1)
print(func_2)

