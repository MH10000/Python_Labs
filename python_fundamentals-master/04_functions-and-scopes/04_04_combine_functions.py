# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    sentence = f"Hello {name}! How are you"
    return sentence

def write_letter(name, text):
    return print(f"{greet(name)} \n{text} \nGoodbye {name}")

write_letter("ben", "it's been a long time")

