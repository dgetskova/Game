from Spell import Spell
from Weapon import Weapon
import random
weapon_bonus = Weapon("Spike", 25)
spell_bonus = Spell("Silver", 30, 7)
mana_bonus = 6,
health_potion_bonus = 10


class Dungeons:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.dungeon = [list(line) for line in lines]
        self.row = 0
        self.col = 0
        self.treasure = {}
        self.get_treasures()

        def get_treasures(self):
            treasure_sequence = self.find_symbol('T')
            for x in treasure_sequence:
                self.treasure[x] = random.choice([mana_bonus, health_potion_bonus,weapon_bonus, spell_bonus])

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

    def find_symbol(self, symbol):
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

    def pick_treasure(self):
        if self.treasure[(self.row, self.col)] == mana_bonus:
            self.hero.take_mana(mana_bonus)
        elif self.treasure[(self.row, self.col)] == health_potion_bonus:
            self.hero.take_healing(health_potion_bonus)
        elif self.treasure[(self.row, self.col)] == weapon_bonus:
            self.hero.equip(self.treasure[(self.row, self.col)])
        else:
            self.hero.learn(self.treasure[(self.row, self.col)])

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
            self.pick_treasure()
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
