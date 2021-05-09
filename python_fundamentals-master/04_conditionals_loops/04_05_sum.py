'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
user_input_low = int(input("Please enter a number: "))
user_input_high = int(input("Please enter a higher number: "))

for n in range(user_input_low, user_input_high+1):
    sum_input = n
    for i in range(user_input_low, user_input_high):
        sum_input += i

print(sum_input)