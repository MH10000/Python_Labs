'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
# Gather user input and create a sorted list
usr_input = input("please enter a list of numbers with a space in between: ")
list1 = list(usr_input.split(" "))
list1.sort()

# Add a zero to the list if it's an odd numbered list 
if len(list1) % 2 != 0:
    list1.append("0")

list2 = list1[0::2]
list3 = list1[1::2]

list4 = zip(list2, list3)
list5 = list(list4)

for tuples in list5:
    print(tuples)