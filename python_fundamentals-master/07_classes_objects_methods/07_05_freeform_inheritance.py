'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Product():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __add__(self, other):
        return self.quantity + other.quantity, self.price + other.price

    def __str__(self):
        return f"{self.quantity} of {self.name} is in stock and cost is USD {self.price}"

class Dental(Product):
    def __init__(self, name, quantity, price, brand):
        super().__init__(name, quantity=0, price=0)
        self.brand = brand

class Gum(Dental):
    def __init__(self, name, quantity, price, brand, flavour):
        super().__init__(name, quantity, price, brand)
        self.flavour = flavour

    def __str__(self):
        return f"Gum = {self.name}, amount = {self.quantity}, price = {self.price}, brand = {self.brand}, flavour = {self.flavour}"
      

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

class Dessert(Food):
    def __init__(self, description, carb_content, protein_content, fat_content):
        super().__init__(description, carb_content, protein_content, fat_content)

    def low_carb(self):
        if self.carb_content < 5:
            return True
        else:
            return False


chocolate_mouse = Dessert("chocolate mousse", 30, 5, 20)
new_gum = Gum("gum", 100, 0.5, "icy blue", "spearmint")
chocolate_mouse_low_carb = Dessert("mint chocolate mouse", 4, 10, 25)

print(chocolate_mouse.low_carb())
print(chocolate_mouse_low_carb.low_carb())
print(chocolate_mouse_low_carb.carb_content)
print(new_gum.flavour)

