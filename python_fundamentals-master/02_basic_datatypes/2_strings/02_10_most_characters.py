'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
# User input
word_1 = input("insert a word ")
word_2 = input("insert another word ")
word_3 = input("and another one ")

# Output
print(len(word_1), word_1)
print(len(word_2), word_2)
print(len(word_3), word_3)

# Defining length variables
len_word_1 = len(word_1)
len_word_2 = len(word_2)
len_word_3 = len(word_3)

# Output challenge
if len_word_1 > len_word_2 and len_word_1 > len_word_3:
    print(word_1, " is the longest word")
elif len_word_2 > len_word_1 and len_word_2 > len_word_3:
    print(word_2, " is the longest word")
else:
     print(word_3, " is the longest word")
     



