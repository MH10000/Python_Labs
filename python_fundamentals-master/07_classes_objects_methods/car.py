class Car():
    """Takes 3 data attributes associated with a car"""
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        """Adds 5 to the speed of the car"""
        self.speed += 5
        
    def brake(self):
        """Reduces speed by 5 with a lower limit of zero"""
        if self.speed < 5:
            self.speed - self.speed
        else:
            self.speed -= 5
        
    def honk_horn(self):
        """Prints a string to honk the horn of the model"""
        return f"{self.model} goes 'beep beep'"
        
my_car = Car("ford", 1985, 4)
my_car.accelerate()
print(my_car.speed)

my_car = Car("Zastava", 2001, 30)
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.speed)

my_car = Car("Rust bucket", 1987)
print(my_car.honk_horn())