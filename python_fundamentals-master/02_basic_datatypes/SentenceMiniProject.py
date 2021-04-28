# Sentence analysis tool that takes user input sentence and outputs:
# number of uppercase letters
# number of lower case letters
# total number of characters
# number of punctuation marks
# Don't count spaces

# User input
user_input = input("Please enter a sentence: ")

# Total characters ouput
total_char = user_input.replace(" ", "")  # Removing spaces
print("Total characters: ", len(total_char)) # Printing length of total characters

# Uppercase and lower case letters output
count_dict = {"Upper case": 0, "Lower case": 0}  # Creating a dictionary to hold number of upper and lower case letters
for upper_case in total_char:                    # looping through the sentence
    if upper_case.isupper():
        count_dict["Upper case"] += 1            # Condition for identifying upper case and adding each instance to the dictionary
    elif upper_case.islower():
        count_dict["Lower case"] += 1            # Condition for identifying lower case and adding each instance to the dictionary
    else:
        pass

# Printing output
print("Upper case: ", count_dict["Upper case"])
print("Lower case: ", count_dict["Lower case"])

# Calculating punctuation count
punct = len(total_char) - count_dict["Upper case"] - count_dict["Lower case"]
print("Punctuation: ", punct)

