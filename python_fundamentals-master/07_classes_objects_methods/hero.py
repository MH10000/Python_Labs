
class Hero():
    """This is the main hero class and defines character parameters as well as damage / heal functions"""
    def __init__(self, name, ability1, ability2, ability3, hp=100):
        self.name = name
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.hp = hp

    def health(self):
        """Health increases hp by 5"""
        self.hp = self.hp + 5
        return f"You found a health potion. hp increased by 5!"

    def take_hit1(self):
        """Hit one reduces hp by 5"""
        self.hp = self.hp - 5
        
    def take_hit2(self):
        """Hit 2 reduces hp by 5"""
        self.hp = self.hp - 10
        
    def take_hit3(self):
        """Hit 2 reduces hp by 15"""
        self.hp = self.hp - 15

    def strike1(self):
        """Attack with ability1"""
        def __str__(self):
            return f"You attack with {self.ability1} and inflict 5 hp damage!"

    def strike1(self):
        """Attack with ability2"""
        def __str__(self):
            return f"You attack with {self.ability2} and inflict 10 hp damage!"

    def strike1(self):
        """Attack with ability3"""
        def __str__(self):
            return f"You attack with {self.ability3} and inflict 15 hp damage!"

class Ninja(Hero):
    """Defines the Ninja class and uses parameters from Hero() superclass"""
    def __init__(self, name, ability1, ability2, ability3, hp=100):
        super().__init__(name, ability1, ability2, ability3, hp=100)

    def __str__(self):
        """Prints the character attributes for the user"""
        return f"Hi {self.name}! You are a Ninja who can {self.ability1}[1], {self.ability2}[2] and {self.ability3}[3]!"

class Ranger(Hero):
    """Defines the Ninja class and uses parameters from Hero() superclass"""
    def __init__(self, name, ability1, ability2, ability3, hp=100):
        super().__init__(name, ability1, ability2, ability3, hp=100)
        
    def __str__(self):
        """Prints the character attributes for the user"""
        return f"Hi {self.name}! You are a Ranger who can {self.ability1}[1], {self.ability2}[2] and {self.ability3}[3]!"


class Villain():
    """Definining the Villain class. Static variable lists exist to lookup villain types and abilities"""
    villains = ["Ogre", "troll", "Deranged mule"]
    abilities5 = ["fist smash", "back hand", "slap", "lazy kick"]
    abilities6 = ["claw stab", "powerful kick", "head butt"]
    def __init__(self, vil_type, ability5, ability6, hp=100):
        self.vil_type = vil_type
        self.ability5 = ability5
        self.ability6 = ability6
        self.hp = hp

    def __str__(self):
        """Text to return upon a vilain encounter"""
        return f"You encounter a {self.vil_type} who can {self.ability5} and {self.ability6}!"

    def vil_attack5(self):
        """Villain attack with ability5"""
        return f"You have been attacked with a {self.ability5} and lose 5 hp!"

    def vil_attack6(self):
        """Villain attack with ability6"""
        return f"You have been attacked with a {self.ability6} and lose 15 hp!"

    def vil_hp_loss1(self):
        """hp Loss on attack 1"""
        self.hp = self.hp - 5

    def vil_hp_loss2(self):
        """hp Loss on attack 1"""
        self.hp = self.hp - 10

    def vil_hp_loss3(self):
        """hp Loss on attack 1"""
        self.hp = self.hp - 15


    

    