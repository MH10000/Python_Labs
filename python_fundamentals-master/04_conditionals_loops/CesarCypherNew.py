# Apply a Cesar cipher to the 'secret' variable

# Import modules
import string
import random

# Obtain user input to get a cypher number incorporating a user input number or random number
secret = input("Enter your text for encryption: ")
cypher_choice = input("Would you like to choose a cypher number? yes or no: ")
cypher = 0
if cypher_choice == "yes":
    cypher = int(input("Enter a number between 1 and 26: "))
else:
    cypher = random.randrange(1, 27)                    # Using the random module to generate a random number

print(f"Your cypher number is {cypher}")

print("Original sentence is:")
print(secret)

secret_lower = secret.lower()                           # Convert all letters to lower case so that we can use one lower case alphabet

# Create the alphabet in a list using the string module
list_alphabet = list(string.ascii_lowercase)

# Create an alphabet list adjusted for the cypher
cypher_alphabet = list(string.ascii_lowercase[(cypher - 1):] + string.ascii_lowercase[:(cypher - 1)])

# create dictionary to replace the alphabet letters with the cypher letter
dict_alphabet = dict(zip(list_alphabet, cypher_alphabet))

cypher_secret = []                                      # Create new variable to store the cypher version of the secret sentence in a list
for letter in secret_lower:                             # loop through original sentence
    if letter not in cypher_alphabet:                   # Condition to identify spaces and punctuation not in the alphabet
        cypher_secret.append(letter)                    # Appends the space, punctuation in it's original form
    else:
        cypher_secret.append(dict_alphabet[letter])     # Looks up the letter in the sentence and appends the cypher replacement letter
        
cypher_secret_sentence = "".join(cypher_secret)         # Converts the cypher list to a sentence

print("Cypher is:")
print(cypher_secret_sentence)