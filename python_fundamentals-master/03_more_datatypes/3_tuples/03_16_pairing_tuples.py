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
# Gather user input and create a list

usr_input = input("please enter a list of numbers with a space in between: ")
list1 = list(usr_input.split(" "))
list1.sort()


# 
new_dict = {}
x = 0
y = 1
new_dict[x] = y
c = 0
while c < len(list1):
    d = list1[x]
    e = list1[y]
    new_dict.update({d, y})
    x += 2
    y += 2
    c += 1

print(new_dict)
new_list1 = []
list_count = len(list1)

d = 0
e = 1

if list_count % 2 == 0:
    for x, y in zip(list1[d], list1[e]):
        new_list.append(x)
        new_list.append(y)
        d += 2
        e += 2

               
else:
    print("odd")

print(new_list)

