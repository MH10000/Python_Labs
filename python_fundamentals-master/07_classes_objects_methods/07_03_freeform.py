'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Product():
    def __init__(self, name, quantity=0, price=0):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __add__(self, other):
        return self.quantity + other.quantity, self.price + other.price


    def __str__(self):
        return f"{self.quantity} of {self.name} is in stock and cost is USD {self.price}"

    

class Shelf():
    def __init__(self, location, length, color):
        self.location = location
        self.length = length
        self.color = color

    def __str__(self):
        return f"This {self.color} shelf is in the {self.location} section and is {self.length}cm long"

class Food():
    def __init__(self, description, carb_content, protein_content, fat_content):
        self.description = description
        self.carb_content = carb_content
        self.protein_content = protein_content
        self.fat_content = fat_content

    def __str__(self):
        return f"This {self.description} has {self.carb_content}g carbs, {self.protein_content}g protein and {self.fat_content}g fat"

toothpaste = Product("toothpaste", 10, 2)
toothbrush = Product("toothbrush", 8, 3)
shelf1 = Shelf("upper", 50, "red")
shelf2 = Shelf("lower", 100, "blue")
steak = Food("sirloin steak", 2, 30, 15)
bread = Food("wholewheat bread", 25, 3, 1)

toothpaste.quantity = 15
shelf1.color = "white"
dental_prod_total = toothpaste + toothbrush

print(toothpaste.quantity)
print(shelf1.color)
print(dental_prod_total)