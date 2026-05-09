import random


class Hero:
    def __init__(self, name, health, lvl, strength):
        self.name = name
        self.health = health
        self.lvl = lvl
        self.strength = strength

    def greet(self): print("Привет")

    def attack(self): print("Удар")

    def rest(self): print("Отдыхает")


class Warrior(Hero):
    def __init__(self, name, health, lvl, strength, stamina):
        super().__init__(name, health, lvl, strength)
        self.stamina = stamina
        self.type = "Warrior"

        def greet(self): print(f"Привет я {self.name}")

    def attack(self): print(f"{self.name} атакует")

    def rest(self): print(f"{self.name} отдыхает")


class Mage(Hero):
    def __init__(self, name, health, lvl, strength, mp):
        super().__init__(name, health, lvl, strength)
        self.mp = mp
        self.type = "Mage"

        def greet(self): print(f"Привет я {self.name}")

    def attack(self): print(f"{self.name} наносит магический удар")

    def rest(self): print(f"{self.name} восстанавливает ману ")


class Assassin(Hero):
    def __init__(self, name, health, lvl, strength, stealth):
        super().__init__(name, health, lvl, strength)
        self.stealth = stealth
        self.type = "Assassin"

        def greet(self): print(f"Я {self.name}!")

    def attack(self): print(f"{self.name} Атакует из-под тишка")

    def rest(self): print(f"{self.name} отдыхает")


axe = Warrior("Axe", 500, 25, 70, 300)
invoker = Mage("Invoker", 600, 10, 50, 450)
riki = Assassin("Riki", 780, 22, 57, 299)
heroes = [axe, invoker, riki]

while True:
    print("\n--- НОВАЯ БИТВА ---")
    print("----- Выберите героя -----")
    print("1.Axe(Warrior)\n2.Invoker(Mage)\n3.Riki(Assassin)")

    while True:
        try:
            choice = int(input("Выберите 1-3: "))
            print("------------------------------")
            if 1 <= choice <= 3:
                break
            print("Ошибка! Введите цифру от 1 до 3")
        except ValueError:
            print("------------------------------\nОшибка!!! Введите число!")

    q_hero = heroes[choice - 1]
    ai_hero = random.choice(heroes)

    print(f"Вы выбрали: {q_hero.type} ({q_hero.name})")
    print(f"Противник: {ai_hero.type} ({ai_hero.name})")

    if q_hero.type == ai_hero.type:
        print("Ничья!")
    elif q_hero.type == "Warrior" and ai_hero.type == "Assassin":
        print(f"{q_hero.name} победил {ai_hero.name}")
    elif q_hero.type == "Assassin" and ai_hero.type == "Mage":
        print(f"{q_hero.name} победил {ai_hero.name}")
    elif q_hero.type == "Mage" and ai_hero.type == "Warrior":
        print(f"{q_hero.name} победил {ai_hero.name}")
    else:
        print(f"Поражение! Выиграл {ai_hero.name}")

    while True:
        play_again = input("------------------------------\nСыграть еще раз? (да/yes или нет/no): ").lower().strip()
        if play_again in ["да", "yes", "y", "д"]:
            break
        elif play_again in ["нет", "no", "n", "н"]:
            print("Спасибо за игру!")
            exit()
        else:
            print("Введите 'да' или 'нет'.")
