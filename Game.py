class GeneralDescription():

    def __init__(self, health, mana):
        self.max_health = 100
        self.max_mana = mana  # 100
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
        if(self.health + healing_points) > self.max_health:
            self.health = 100

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


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:

    def __init__(self, name, damage, required_mana):
        self.name = name
        self.damage = damage
        self.required_mana = required_mana


class Hero (GeneralDescription, Spell, Weapon):

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


class Enemy(GeneralDescription):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage


class Dungeons:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.dungeon = [list(line) for line in lines]
        self.x = -1
        self.y = -1

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def starting_point(self, S):
        pass

    def spawn(self):
        found = False
        for i in range(0, len(self.dungeon)):
            for j in range(0, len(self.dungeon[i])):
                if self.dungeon[i][j] == "S":
                    self.dungeon[i][j] = "H"
                    self.x = i
                    self.y = j
                    found = True
                    break
            if found:
                break
            return found

    def find_symbol(self, symbol):
        print(type(self.dungeon))
        line_index = 0
        for line in self.dungeon:
            elem_index = 0
            for elem in line:
                if elem == symbol:
                    return [line_index, elem_index]
                elem_index += 1
            line_index += 1

    def move_hero(self, directions):
        self.directions = directions

    def move_up(self):
        check = True
        if self.y - 1 < 0:
            check = False
        elif self.dungeon[self.y - 1][self.x] == '.':
            temp = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = self.dungeon[self.y - 1][self.x]
            self.dungeon[self.y - 1][self.x] = temp
            self.y -= 1
        elif self.dungeon[self.y - 1][self.x] == '#':
            check = False
        elif self.dungeon[self.y - 1][self.x] == 'T':
            self.dungeon[self.y][self.x] = "."
            # absorb treasure
            self.dungeon[self.y - 1][self.x] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.y -= 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_down(self):
        check = True
        if self.y + 1 > len(self.dungeon) - 1:
            check = False
        elif self.dungeon[self.y + 1][self.x] == '.':
            temp = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = self.dungeon[self.y + 1][self.x]
            self.dungeon[self.y + 1][self.x] = temp
            self.y += 1
        elif self.dungeon[self.y + 1][self.x] == '#':
            check = False
        elif self.dungeon[self.y + 1][self.x] == 'T':
            # absorb treasure
            self.dungeon[self.y + 1][self.x] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.y += 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_left(self):
        check = True
        if self.x - 1 < 0:
            check = False
        elif self.dungeon[self.y][self.x - 1] == '.':
            temp = self.dungeon[self.y][self.x - 1]
            self.dungeon[self.y][self.x - 1] = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = temp
            self.x -= 1
        elif self.dungeon[self.y][self.x - 1] == '#':
            check = False
        elif self.dungeon[self.y][self.x - 1] == 'T':
            # absorb treasure
            self.dungeon[self.y][self.x - 1] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.x -= 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_right(self):
        check = True
        if self.x + 1 > len(self.dungeon[0]) - 1:
            check = False
        elif self.dungeon[self.y][self.x + 1] == ".":
            temp = self.dungeon[self.y][self.x + 1]
            self.dungeon[self.y][self.x + 1] = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = temp
            self.x += 1
        elif self.dungeon[self.y][self.x + 1] == "#":
            check = False
        elif self.dungeon[self.y][self.x + 1] == 'T':
            # absorb treasure
            self.dungeon[self.y][self.x + 1] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.x += 1
        else:
            # Fight
            print("Let's fight")
        return check


a = Dungeons("map.txt")
a.print_map()
a.spawn()
print("------------------------")
a.print_map()
didi = Hero()
didi.equip(Weapon("Asda", 50))
didi.learn(Spell("spell", 50, 5))
