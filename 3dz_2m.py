from abc import ABC, abstractmethod


class Hero(ABC):
    @abstractmethod
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


print()


class Warrior(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        print(f"Привет я {self.name}")

    def attack(self):
        return "Воин атакует мечом"


axe = Warrior("Акс", 24, 3800, 79)
axe.greet()
axe.rest()
print(axe.attack())
print()


class Mage(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        print(f"Привет!! Я {self.name}")

    def attack(self):
        return "Маг использует магию"


invoker = Mage("Инвокер", 27, 2800, 64)
invoker.greet()
invoker.rest()
print(invoker.attack())
print()


class Assassin(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        print(f"Привет!!! Меня зовут {self.name}")

    def attack(self):
        return "Ассасин атакует из-под тишка"


phantom_assassin = Assassin("Мортра", 29, 3200, 55)
phantom_assassin.greet()
phantom_assassin.rest()
print(phantom_assassin.attack())
