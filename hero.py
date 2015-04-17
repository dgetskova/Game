class GeneralDescription():
    def __init__(self, health, mana):
        self.max_health = 100
        self.max_mana = mana
        self.health = health
        self.mana = mana

    def is_alive(self):
        return self.health != 0

    def can_cast():
        pass

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if(self.health + healing_points) >= self.max_health:
            return False

        self.health += healing_points
        return True

    def take_mana(self):
        pass
        # pri vseki hod da se povishava manata
        # pri piene na neshto pak se povishava
        # ne moje da e poveche ot purvonachalnata max mana

    def attack(self):
        pass
# by="weapon") - returns the damage of the weapon if equiped or 0 otherwise
# by="magic") - returns the damage of the spell, if quiped or 0 otherwise

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0


class Hero (GeneralDescription):
    def __init__(self, name="Didka", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        GeneralDescription.__init__(self, health, mana)
        self.__name = name
        self.__title = title
        # self.__health = health
        # self.__mana = mana
        self.__manaregeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{0} the {1}".format(self.__name, self.__title)


class Enemy(GeneralDescription):
    pass