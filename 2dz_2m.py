class Hero:

    def __init__(self, name, lvl, hp, strength, mp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength
        self.mp = mp

    def action(self):
        print(f"{self.name} base action")

class Mage(Hero):

    def __init__(self, name, lvl, hp, strength, mp):
        super().__init__(name, lvl, hp, strength, mp)

    def attack(self):
        print("Удар")
    def greet(self):
        print("!")
    def rest(self):
        print(f"Дай отдохнуть {self.name}")
