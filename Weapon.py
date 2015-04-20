class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:

    def __init__(self, name, damage, required_mana):
        self.name = name
        self.damage = damage
        self.required_mana = required_mana
