from hero import Hero, Villain, Ninja, Ranger
import random




user_unput_hero = input("Please choose your hero! Do you want to be a Ninja or a Ranger? ")
user_name = input("Excellent choice, what is your hero's name? ")

ninja = Ninja(user_name, "Judo chop", "Side kick", "Sword strike")
ranger = Ranger(user_name, "eye poke", "knife strike", "shoot arrows")

if user_unput_hero == "Ninja" or "ninja":
    print(ninja.__str__())
else:
    print(ranger.__str__())


villain1 = Villain(villains[random.randrange(0, 2)], self.abilities5[random.randrange(0, 2)], self.abilities6[random.randrange(0, 2)])
print(villain1)
