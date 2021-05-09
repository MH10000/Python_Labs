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
v = 0
dict_ = dict.fromkeys(set_list, v)

for k in dict_:
    if k in input_2list:
        v = input_2list.count(k)
        dict_[k] = v
    else:
        pass

print(input_2list)
print(dict_)