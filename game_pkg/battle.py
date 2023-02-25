from game_pkg.menu import *
from game_pkg.player import *
from game_pkg.constants import *


def battle(player, enemy):
    input(FIGHT)
    while enemy.hp > 0 and player.hp > 0:
        enemy.takedamage(player)
        player.takedamage(enemy)
