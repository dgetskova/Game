import random


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

    def take_mana(self, mana_points):
        if self.mana + mana_points > 100:
            self.mana = 100
        self.mana += mana_points

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

    def __init__(self, name, damage, required_mana,cast):
        self.name = name
        self.damage = damage
        self.required_mana = required_mana


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

    def find_symbol_treasure(self, symbol):
        print(type(self.dungeon))
        positions = []
        line_index = 0
        for line in self.dungeon:
            elem_index = 0
            for elem in line:
                if elem == symbol:
                    # return [(line_index, elem_index)]  # touple ot pozicii
                    positions.append((line_index, elem_index))
                elem_index += 1
            line_index += 1
        return positions



    def is_in_bound(self, positions):
        # positions = [row, col]
        count_row = len(self.dungeon)
        count_col = len(self.dungeon[0])
        return (positions[0] >= 0 and positions[0] < count_row)\
            and (positions[1] >= 0 and positions[1] < count_col)

    def return_what_found_while_moving(self, symbol):
        if symbol == 'G':
            return "You are the best ^_^ End of level!"

        if symbol == '.':
            return True
        if symbol == 'T':

            return "You found treasure"

        if symbol == 'E':
            # make fight
            return "Fight! Let the better win!"

    def make_move(self, old_positions, new_positions):
        new_row = new_positions[0]
        new_col = new_positions[1]
        old_row = old_positions[0]
        old_col = old_positions[1]
        if self.is_in_bound(new_positions):
            if self.dungeon[new_row][new_col] is not'#':
                to_return = self.return_what_found_while_moving(
                    self.dungeon[new_row][new_col])
                self.dungeon[old_row][old_col] = '.'
                self.dungeon[new_row][new_col] = 'H'
            else:
                return False
        else:
            return False

        self.row = new_row
        self.col = new_col
        return to_return

    def is_valid_move(self, directions):
        if directions == "up":
            return self.make_move([self.row, self.col], [self.row - 1, self.col])

        elif directions == "down":
            return self.make_move([self.row, self.col], [self.row + 1, self.col])

        elif directions == "left":
            return self.make_move([self.row, self.col], [self.row, self.col - 1])

        elif directions == "right":
            return self.make_move([self.row, self.col], [self.row, self.col + 1])

    def move_hero(self, directions):
        if directions in ["up", "down", "left", "right"]:
            return self.is_valid_move(directions)
            self.mana += self.mana_regeneration_rate
        else:
            print("Wrong input!")

    def pick_treasure(self):

        weapon_bonus = Weapon("Spike", 25)
        spell_bonus = Spell("Silver", 30, 7)
        mana_bonus = 6,
        health_potion_bonus = 10

        T = random.choice(
            [mana_bonus, health_potion_bonus, weapon_bonus, spell_bonus])
        if T == mana_bonus:
            self.hero.take_mana(mana_bonus)
        elif T == health_potion_bonus:
                self.hero.take_healing(health_potion_bonus)
        elif T == weapon_bonus:
            self.hero.equip(T)
        else:
            self.hero.learn(T)
a = Dungeons("map.txt")
a.print_map()
a.spawn()
print("------------------------")
a.print_map()
didi = Hero()
didi.equip(Weapon("Asda", 50))
didi.learn(Spell("spell", 50, 5))
hero = Hero()
print(hero.known_as())
print(a.pick_treasure())
w = Weapon("Silver", 50)
print("---------------------------")
didi.equip(w)
