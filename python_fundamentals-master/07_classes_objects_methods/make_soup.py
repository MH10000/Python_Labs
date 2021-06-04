class Ingredient:
    """Models an ingredient including its name and amount."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"There are {self.amount} of {self.name}."

    def use(self, use_amount):
        self.amount -= use_amount

class Soup:
    def __init__(self, ingredient_ls):
        self.ingredient_ls = ingredient_ls
        self.name = ""
        self.serves = 0

    def cook(self):
        for item in self.ingredient_ls:
            self.name += item.name[3:]
            self.serves += (len(self.ingredient_ls))/1.5

    def __str__(self):
        return f"This is a {self.name} soup and serves {self.serves}!"

carrot = Ingredient("Carrot", 4)
peas = Ingredient("peas", 20)
noodles = Ingredient("noodles", 50)

food_list = [carrot, peas, noodles]
new_soup = Soup(food_list)
new_soup.cook()
print(carrot.name)
print(new_soup.__str__())

