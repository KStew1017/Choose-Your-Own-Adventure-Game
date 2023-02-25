import math


def player_menu(player):

    while True:
        print(f"""
***********************************************************************
_______________________________________________________________________

You are {player.name}

Stats:

HP: {player.hp}/{player.maxhp}
Armor: {round(player.armor)}
Damage: {player.damage}
        
Potions:
""")

        if len(player.items) == 0:
            print("--- You have no potions ---")
        else:
            i = 0
            for potion in player.items:
                potion = f"{player.items[i][0]}: {player.items[i][1]}"
                i += 1
                print(f"    {i}) {potion}")

        print("""
_______________________________________________________________________""")

        use_item = input("\nUse Item? ( Y / N ): ")
        if use_item.lower() == "y":
            item_choice = input("Select a Potion: ")
            player.usepotion(item_choice)
        if use_item.lower() == "n":
            input("\nExit (Enter any key) ")
            break


def invoke_menu(player):
    while True:
        menu = input("\nGo to menu? ( Y / N ): ")
        if menu.lower() == "y":
            player_menu(player)
            break
        elif menu.lower() == "n":
            break
        else:
            print("Please choose Y or N")
            continue
