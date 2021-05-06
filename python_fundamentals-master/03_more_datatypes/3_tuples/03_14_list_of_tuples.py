'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# Get user input
sentence = input("write a sentence: ")

# Create list from string
list1 = list(sentence.split(" "))

# loop through list to create tuples in new list
list2 = []
y = 0
for x in list1:
    z = tuple(list1[y])    # Create new tuple during each loop
    y += 1                 # move along to next index in list
    list2 += z,            # Add tuple to new list

print(list2)