'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
user_input = int(input("Please enter a number between 0 and 1,000,000,000: "))

i = 0
while i < 1000000000:
    if i == user_input:
        print(i)
        break
    i += 1