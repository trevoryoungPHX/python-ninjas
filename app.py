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

kevTheNinja = Ninja("Kevin")
kevTheNinja.eat()
print(kevTheNinja.health)
