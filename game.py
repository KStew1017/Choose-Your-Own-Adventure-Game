from game_pkg.player import initialize_player
from game_pkg.menu import player_menu, invoke_menu
from game_pkg.randomize import random_item
from game_pkg.battle import battle
from game_pkg.characters import *
from game_pkg.items import *
from game_pkg.constants import *
import random


print(WORLD_BACK_STORY)
input(CONTINUE)

print(GAME_BACK_STORY)
input(CONTINUE)

player = None

while player is None:
    player = initialize_player()
    print(f"\nYou have chosen to be {player.name}!")

player.addpotion("Health Potion")

invoke_menu(player)

print(LOOT_SHIPWRECK)
while True:
    loot_shipwreck = input(LOOT_SHIPWRECK_INPUT)
    if loot_shipwreck.lower() == "y":
        print(LOOT_SHIPWRECK_YES_1)
        random_item(player)
        break
    elif loot_shipwreck.lower() == "n":
        break
    else:
        print(CHOOSE_VALID_OPTION)
        continue

invoke_menu(player)

print(PIRATE_SHIP)
while True:
    confront_pirate_ship = input(PIRATE_SHIP_INPUT)
    if confront_pirate_ship.lower() == "confront":
        pirate1 = CommonPirate(100, 50, 20)
        print(PIRATE_CONFRONT_1)
        battle(player, pirate1)
        if player.hp > 0:
            print(PIRATE_CONFRONT_2)
            random_item(player)
            break
        else:
            print(YOU_DIED)
            exit()
    elif confront_pirate_ship.lower() == "sail around":
        break
    else:
        print(CHOOSE_VALID_OPTION)
        continue

invoke_menu(player)

print(LAND_ON_TOL_NAMMA)
while True:
    north_or_south = input(LAND_ON_TOL_NAMMA_INPUT)

#####################################################################################
# NORTH

    if north_or_south.lower() == "north":
        print(NORTH_PIRATE)
        while True:
            north_pirate = input(NORTH_PIRATE_INPUT)
            if north_pirate.lower() == "fight":
                pirate2 = CommonPirate(100, 50, 20)
                print(PIRATE_CONFRONT_1)
                battle(player, pirate2)
                if player.hp > 0:
                    print(PIRATE_CONFRONT_2)
                    random_item(player)
                    break
                else:
                    print(YOU_DIED)
                    exit()
            elif north_pirate.lower() == "pass":
                break
            else:
                print(CHOOSE_VALID_OPTION)
                continue

        invoke_menu(player)

        brute1 = BrutePirate(200, 50, 30)
        print(NORTH_BRUTE)
        input(CONTINUE)
        print(BRUTE_CONFRONT_1)
        battle(player, brute1)
        if player.hp > 0:
            print(PIRATE_CONFRONT_2)
            random_item(player)
        else:
            print(YOU_DIED)
            exit()

        invoke_menu(player)

        print(NORTH_VOLCANO)
        while True:
            volcano = input(NORTH_VOLCANO_INPUT)
            if volcano.lower() == "lava":
                player.hp = player.hp - 20
                if player.hp > 0:
                    print(NORTH_VOLCANO_LAVA)
                    random_item(player)
                    break
                else:
                    print(YOU_DIED)
                    exit()
            elif volcano.lower() == "safe":
                break
            else:
                print(CHOOSE_VALID_OPTION)
                continue

        invoke_menu(player)

        break

#####################################################################################
# SOUTH

    elif north_or_south.lower() == "south":
        print(SOUTH_PIRATE)
        while True:
            south_pirate = input(SOUTH_PIRATE_INPUT)
            if south_pirate.lower() == "fight":
                pirate3 = CommonPirate(100, 50, 20)
                print(PIRATE_CONFRONT_1)
                battle(player, pirate3)
                if player.hp > 0:
                    print(PIRATE_CONFRONT_2)
                    random_item(player)
                    break
                else:
                    print(YOU_DIED)
                    exit()
            elif south_pirate.lower() == "Pass":
                break
            else:
                print(CHOOSE_VALID_OPTION)
                continue

        invoke_menu(player)

        brute2 = BrutePirate(200, 50, 30)
        print(SOUTH_BRUTE)
        input(CONTINUE)
        print(BRUTE_CONFRONT_1)
        battle(player, brute2)
        if player.hp > 0:
            print(BRUTE_CONFRONT_2)
            random_item(player)
        else:
            print(YOU_DIED)
            exit()

        invoke_menu(player)

        brute3 = BrutePirate(200, 50, 30)
        print(SOUTH_BRUTE_2)
        input(CONTINUE)
        print(BRUTE_CONFRONT_1)
        battle(player, brute3)
        if player.hp > 0:
            print(BRUTE_CONFRONT_2)
            random_item(player)
        else:
            print(YOU_DIED)
            exit()

        invoke_menu(player)

        break

#####################################################################################

    else:
        print(CHOOSE_VALID_OPTION)

print(PIRATE_LEADER)
invoke_menu(player)

leader = PirateLeader(150, 150, 40)
print(LEADER_CONFRONT_1)
battle(player, leader)
if player.hp > 0:
    print(LEADER_CONFRONT_2)
    print(COMPLETE_GAME)
    print(f"""
Final Stats:

HP: {player.hp}/{player.maxhp}
Armor: {round(player.armor)}
Damage: {player.damage}
""")
    print(SEPARATOR)
else:
    print(YOU_DIED)
    exit()
