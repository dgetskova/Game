from Game import GeneralDescription


class Enemy(GeneralDescription):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage
