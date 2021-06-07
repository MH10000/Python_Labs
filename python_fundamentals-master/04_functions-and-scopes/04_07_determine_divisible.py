# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def div_or(n):
    if n % 4 ==0 or n % 7 == 0:
        return f"{n} is divisible by 4 or 7"
    else:
        return f"{n} is not divisible by 4 or 7"

def div_and(n):
    if n % 4 == 0 and n % 7 == 0:
        return f"{n} is divisible by 4 and 7"
    else:
        return f"{n} is not divisible by 4 and 7"

user_input = int(input("please snter a number between 1 and 1,000,000,000"))
input_or = div_or(user_input)
input_and = div_and(user_input)
print(f"{input_or} and {input_and}")
