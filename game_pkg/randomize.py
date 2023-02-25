from game_pkg.characters import *
from game_pkg.constants import *
import random


def random_item(player):
    i = random.randint(1, 3)
    if i == 1:
        player.newarmor()
    elif i == 2:
        player.newdamage()
    elif i == 3:
        j = random.randint(1, 3)
        if j == 1:
            player.addpotion("Health Potion")
            print(FOUND_HEALTH_POTION)
        elif j == 2:
            player.addpotion("Large Health Potion")
            print(FOUND_LARGE_HEALTH_POTION)
        elif j == 3:
            player.addpotion("Super Health Potion")
            print(FOUND_SUPER_HEALTH_POTION)
