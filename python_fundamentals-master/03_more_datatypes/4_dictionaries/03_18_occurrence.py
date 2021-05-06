'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
# User input
user_input = input("please enter a sentence: ")
input_2 = user_input.replace(" ", "")
input_2list = list(input_2)
set_input = set(input_2)                # Create a set to eliminate duplicate characters
set_list = list(set_input)              # Convert set to list

# Dictionary creation and input pairs
dict_ = {}                              # Create empty dictionary
x = 0                                   # Define variables 
y = 0
z = 0
dict_[x] = y                            # Define dict pairs. But this creates a forst pair as 0:0. How do I avoid doing this?

while z < len(set_list):
    b = set_list[x]                     # Reference x index in set_list
    dict_.update({b: y})                # Update pair in dictionary.
    x += 1                              # Add 1 to x so that the loop moves to next index in set_list
    z += 1                              # Add 1 to z to end loop once list has been looped through

# Count characters and add vales to dict_

for d in dict_:
    c = input_2list.count(d)
    dict_[d] = c

dict_.pop(0)                            # Remove the unwanted 0:0 from the dictionary

print(dict_)