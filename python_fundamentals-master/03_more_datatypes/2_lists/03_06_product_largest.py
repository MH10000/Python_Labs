'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

# collect user inputs
num_1 = int(input("please input a number: "))
num_2 = int(input("please input another number: "))
num_3 = int(input("please input another number: "))
num_4 = int(input("please input another number: "))
num_5 = int(input("please input another number: "))
num_6 = int(input("please input another number: "))
num_7 = int(input("please input another number: "))
num_8 = int(input("please input another number: "))
num_9 = int(input("please input another number: "))
num_10 = int(input("please input another number: "))

# add user inputs to the list
usr_list = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]

# Sort list
usr_list.sort()

print(usr_list[-1])

# Calculate product of the list
p = 1
for i in usr_list:
    p *= i

print(p)



