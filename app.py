from random import randint

class Human:
    health = 30
    name = ""
    def __init__(self, name):
        self.name = name

    def eat(self):
        self.health+=5

myHuman = Human("Hassan")
myHuman.eat()
print(myHuman.health)

class Ninja(Human):
    health = 10
    def __init__(self, name):
        Human.__init__(self, name)

    def meditate(self):
        self.health+=10

    def backstab(self, obj):
        obj.health-=10

kevTheNinja = Ninja("Kevin")
kevTheNinja.backstab(myHuman)
print(kevTheNinja.health)
print(myHuman.health)



class Wizzard(Human):
    health = 25
    magicPower = 0
    def __init__(self, name):
        Human.__init__(self, name)

    def study(self):
        self.magicPower+=(randint(1, 3))

    def fireball(self, target):
        target.health-=self.magicPower

trevTheWizzard = Wizzard("Trevor")
trevTheWizzard.study()
print(trevTheWizzard.magicPower)


class Warrior(Human):
    health = 40
    armor = 10
    def __init__(self, name):
        Human.__init__(self, name)

    def armorUp(self):
        self.armorUp+=5

    def shieldAlly(self, ally):
        self.armor-=5
        ally.health+=5
