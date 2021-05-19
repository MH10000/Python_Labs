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

# Create the alphabet using the string module
alphabet_ = string.ascii_lowercase

# Create an alphabet adjusted for the cypher
cypher_alphabet = string.ascii_lowercase[(cypher - 1):] + string.ascii_lowercase[:(cypher - 1)]

# Make a table to translate the original alphabet to the cypher alphabet using the maketrans() method
my_table = alphabet_.maketrans(alphabet_, cypher_alphabet)

print("Cypher is:")
print(secret_lower.translate(my_table))                       # Use the translate() method to convert the phrase to the cypher using the table