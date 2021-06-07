# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(type_bread, *args):
    toppings = ""
    for topping in args:
        toppings += topping + "\n"
    
    return f"{type_bread}\n{toppings}{type_bread}"

print(make_sandwich("bloomer bread", "mayo", "ham", "cheese"))