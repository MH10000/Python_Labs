'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
class Movie():
    def __init__(self, year, title):
        self.year = year
        self.title = title

class Romcom(Movie):
    def __init__(self, year, title, main_actor):
        super().__init__(year, title)
        self.main_actor = main_actor

    def cry(self):
        if self.main_actor == "Jenny":
            print("cry")
        else:
            print("laugh")

class ActionMovie(Movie):
    pg = 13
    def __init__(self, main_actor):
        self.main_actor = main_actor

lovenote = Romcom(1985, "November Rain", "Rose")
action1 = ActionMovie("Arnie")
print(action1.main_actor)
print(lovenote.title)
print(lovenote.cry())