from game_pkg.characters import *


def initialize_player():
    print(
        """
***************************************************************************************
_______________________________________________________
|   1) Crean:     |   2) Drorant:   |   3) Eldalian:  |
|                 |                 |                 |
|   HP = 100      |   HP = 200      |   HP = 150      |
|   Armor = 120   |   Armor = 0     |   Armor = 60    |
|   Damage = 30   |   Damage = 50   |   Damage = 40   |
|_________________|_________________|_________________|
"""
    )
    choice = input("Choose a character: ")
    if choice.lower() == "crean" or choice == "1":
        return Crean(100, 120, 30)
    elif choice.lower() == "drorant" or choice == "2":
        return Drorant(200, 0, 50)
    elif choice.lower() == "eldalian" or choice == "3":
        return Eldalian(150, 60, 40)
    else:
        print("\nPlease choose again from the available characters")
        return None
