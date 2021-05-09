# Apply a Cesar cipher of 7 to the 'secret' variable

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

print("Original sentence is:")
print(secret)

secret_lower = secret.lower()                           # Convert all letters to lower case so that we can use one lower case alphabet

# Create the alphabet in a list
list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Create the cypher alphabet - start at "g" which moves the start of the alphabet 7 spaces
cypher_alphabet = ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f"]


# create dictionary to replace the alphabet letters with the cypher letter
dict_alphabet = dict.fromkeys(list_alphabet, 0)

replacement_ = 0                                        # Create variable to store index position of the cypher alphabet
for k in dict_alphabet:                                 # for loop to get through entire dictionary
    dict_alphabet[k] = cypher_alphabet[replacement_]    # replace zero value in original dictionary with teh cypher alphabet letter
    replacement_ += 1                                   # increase "replacement" variable by 1 to move to next index position on next loop

cypher_secret = []                                      # Create new variable to store the cypher version of the secret sentence in a list
for letter in secret_lower:                             # loop through original sentence
    if letter not in cypher_alphabet:                   # Condition to identify spaces and punctuation not in the alphabet
        cypher_secret.append(letter)                    # Appends the space, punctuation in it's original form
    else:
        cypher_secret.append(dict_alphabet[letter])     # Looks up the letter in the sentence and appends the cypher replacement letter
        
cypher_secret_sentence = "".join(cypher_secret)         # Converts the cypher list to a sentence

print("Cypher is:")
print(cypher_secret_sentence)