'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
# User input
str1 = input("enter a sentence: ")

str_list = list(str1.split(" ")) # Create list from user input and split string on space delimiter

most_dict = dict.fromkeys(str_list, 0)  # Create dictionary with the keys being the unique list items
for x in str_list:                      # loop through list created from the sentence
    count = 0                           # Create variable to count instances of items in list
    for y in str_list:                  # loop again to compare x to y
        if y == x:                      # Conditional to apply if true
            count += 1                  # Add to count if true
    most_dict[x] += 1                   # Add 1 in value to the key
    
values = list(most_dict.values())       # Creates a list of the values from the dict
keys = list(most_dict.keys())           # Creates a list of the keys from the dict

m = max(values)                         # Finds the highest value in the list of values
i = values.index(m)                     # Refers to the index position of the highest value

print(keys[i])                          # Prints the key with the highest value 


