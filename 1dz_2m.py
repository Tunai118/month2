class Hero:

    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength
    def greet(self):
        return f"Привет я {self.name}, мой уровень {self.lvl}"

    def attack(self,enemy):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1

        pass

djabrail = Hero("Джабраил", 21, 100, 15)
magomed = Hero("Магомед", 22, 100, 19)

print(f"--- статы {djabrail.name}(a): Сила {djabrail.strength}, хп {djabrail.health}")
djabrail.greet()
djabrail.attack(1)
print(f"--- статы {djabrail.name}(a): Сила после удара {djabrail.strength}, хп после {djabrail.health}")
djabrail.rest()
print(f"хп после {djabrail.health}")

print(f"--- статы {magomed.name}(a: Сила {magomed.strength}, хп {magomed.health}")
magomed.greet()
magomed.attack(1)
print(f"--- статы {magomed.name}(a): Сила после удара {magomed.strength}, хп после {magomed.health}")
magomed.rest()
print(f"хп после {magomed.health}")







