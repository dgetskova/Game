from Game import GeneralDescription
from Spell import Spell
from Weapon import Weapon


class Hero (GeneralDescription):

    def __init__(self, name="Didka", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        super().__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__weapon = Weapon("", 0)
        self.__spell = Spell("", 0, 0)

    def known_as(self):
        return "{0} the {1}".format(self.__name, self.__title)

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
            print(self.__weapon.name)

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.__spell = spell
            print(self.__spell.name)

