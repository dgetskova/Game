# from Map import Dungeons
from Hero import Enemy
from Hero import Hero


class Fight:
    def __init__(self, hero, enemy):
        if not(isinstance(hero, Hero()) or isinstance(enemy, Enemy())):
            raise ValueError

        while hero.is_alive() or enemy.is_alive():
            hero.attack()
            enemy.take_damage()
            if enemy.is_alive:
                enemy.attack()
                hero.take_damage()


