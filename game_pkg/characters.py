from game_pkg.items import *
from game_pkg.constants import *
import random


########## Character Classes ##########

class Character:
    def __init__(self, hp, armor, damage):
        self.hp = hp
        self.maxhp = hp
        self.armor = armor
        self.damage = damage
        self.items = []

    def newarmor(self):
        chance = random.randint(1, 100)
        if (1 <= chance <= 40):
            if self.armor >= armor[LEATHER_ARMOR]:
                self.armor
                print(YOU_HAVE_BETTER_ARMOR)
            else:
                self.armor = armor[LEATHER_ARMOR]
                print(FOUND_LEATHER_ARMOR)
        elif (41 <= chance <= 70):
            if self.armor >= armor[STEEL_ARMOR]:
                self.armor
                print(YOU_HAVE_BETTER_ARMOR)
            else:
                self.armor = armor[STEEL_ARMOR]
                print(FOUND_STEEL_ARMOR)
        elif (71 <= chance <= 85):
            if self.armor >= armor[GOLD_ARMOR]:
                self.armor
                print(YOU_HAVE_BETTER_ARMOR)
            else:
                self.armor = armor[GOLD_ARMOR]
                print(FOUND_GOLD_ARMOR)
        elif (86 <= chance <= 95):
            if self.armor >= armor[OBSIDIAN_ARMOR]:
                self.armor
                print(YOU_HAVE_BETTER_ARMOR)
            else:
                self.armor = armor[OBSIDIAN_ARMOR]
                print(FOUND_OBSIDIAN_ARMOR)
        elif (96 <= chance <= 100):
            if self.armor >= armor[DAEGOLIC_ARMOR]:
                self.armor
                print(YOU_HAVE_BETTER_ARMOR)
            else:
                self.armor = armor[DAEGOLIC_ARMOR]
                print(FOUND_DAEGOLIC_ARMOR)

    def newdamage(self):
        chance = random.randint(1, 100)
        if (1 <= chance <= 44):
            if self.damage >= weapons[IRON_DAGGERS]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[IRON_DAGGERS]
                print(FOUND_IRON_DAGGERS)
        elif (45 <= chance <= 69):
            if self.damage >= weapons[STEEL_SWORD]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[STEEL_SWORD]
                print(FOUND_STEEL_SWORD)
        elif (70 <= chance <= 84):
            if self.damage >= weapons[GOLD_SWORD]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[GOLD_SWORD]
                print(FOUND_GOLD_SWORD)
        elif (85 <= chance <= 94):
            if self.damage >= weapons[OBSIDIAN_KATANA]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[OBSIDIAN_KATANA]
                print(FOUND_OBSIDIAN_KATANA)
        elif (95 <= chance <= 99):
            if self.damage >= weapons[DAEGOLIC_LONGSWORD]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[DAEGOLIC_LONGSWORD]
                print(FOUND_DAEGOLIC_LONGSWORD)
        elif (chance == 100):
            if self.damage >= weapons[OVALIAN_GREATSWORD]:
                self.damage
                print(YOU_HAVE_BETTER_WEAPON)
            else:
                self.damage = weapons[OVALIAN_GREATSWORD]
                print(FOUND_OVALIAN_GREATSWORD)

    def addpotion(self, item):
        potion = [item, potions[item]]
        if len(self.items) <= 4:
            self.items.append(potion)

    def usepotion(self, item):
        if self.hp == self.maxhp:
            self.hp
        if item == "1":
            self.hp += potions[self.items[0][0]]
            self.items.pop(0)
            if self.hp >= self.maxhp:
                self.hp = self.maxhp
        elif item == "2":
            self.hp += potions[self.items[1][0]]
            self.items.pop(1)
            if self.hp >= self.maxhp:
                self.hp = self.maxhp
        elif item == "3":
            self.hp += potions[self.items[2][0]]
            self.items.pop(2)
            if self.hp >= self.maxhp:
                self.hp = self.maxhp
        elif item == "4":
            self.hp += potions[self.items[3][0]]
            self.items.pop(3)
            if self.hp >= self.maxhp:
                self.hp = self.maxhp

    def takedamage(self, enemy):
        if self.armor > 0:
            armordamage = (enemy.damage * 0.75)
            self.armor = self.armor - armordamage
            if self.armor <= 0:
                self.hp = self.hp + (self.armor / 0.75)
                self.hp = round(self.hp)
                self.armor = 0
        else:
            self.hp = self.hp - enemy.damage


class Crean(Character):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Crean"


class Drorant(Character):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Drorant"


class Eldalian(Character):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Eldalian"

########## Enemy Classes ##########


class Enemy:
    def __init__(self, hp, armor, damage):
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def takedamage(self, enemy):
        if self.armor > 0:
            armordamage = (enemy.damage * 0.75)
            self.armor = self.armor - armordamage
            if self.armor <= 0:
                self.hp = self.hp + (self.armor / 0.75)
                self.hp = round(self.hp)
                self.armor = 0
        else:
            self.hp = self.hp - enemy.damage


class CommonPirate(Enemy):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Common Pirate"


class BrutePirate(Enemy):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Brute Pirate"


class PirateLeader(Enemy):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
        self.name = "Pirate Leader"
