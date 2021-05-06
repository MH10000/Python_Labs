'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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

# Return list in new order
print(usr_list[1], usr_list[3], usr_list[5], usr_list[7], usr_list[9], usr_list[8], usr_list[6], usr_list[4], usr_list[2], usr_list[0])

