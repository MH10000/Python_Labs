'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
# User input
sentence = input("enter a sentence ")

# Find vowels
vowels = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")
print(vowels)

# Challenge new user input
print("Challenge!")
next_sentence = input("enter a new sentence ")
vowel_a = str(next_sentence.count("a"))
vowel_e = str(next_sentence.count("e"))
vowel_i = str(next_sentence.count("i"))
vowel_o = str(next_sentence.count("o"))
vowel_u = str(next_sentence.count("u"))
print("a = " + vowel_a + " times")
print("e = " + vowel_e + " times")
print("i = " + vowel_i + " times")
print("o = " + vowel_o + " times")
print("u = " + vowel_u + " times")
