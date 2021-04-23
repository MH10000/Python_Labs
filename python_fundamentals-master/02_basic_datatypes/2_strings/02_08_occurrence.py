'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
# User input
string = input("enter sentence ")
letter = input("enter a letter ")

# Find index
position = string.find(letter)
print(position)
