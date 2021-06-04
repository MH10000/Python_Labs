# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys

password = "greentree"

pword = None
while pword != password:
    pword = input("enter the password or type 'quit' to exit: ")
    if pword == password:
        print("Correct, you may enter")
        break
    else:
        if pword == "quit":
            quit()

