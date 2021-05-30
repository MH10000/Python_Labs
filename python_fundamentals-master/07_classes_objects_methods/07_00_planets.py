'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"The planet {self.name} is {self.color} and is in the {self.system}"

    def bears_life(self):
        return self.color.lower() == "blue"


mars = Planet("Mars", "red", "solar system")
print(mars.bears_life())
