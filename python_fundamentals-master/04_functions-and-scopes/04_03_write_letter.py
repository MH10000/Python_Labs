# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    return print(f"Hi {name} \n{text} \nGoodbye {name}")

write_letter("ben", "I hope things are going well, what have you been up to?") 


