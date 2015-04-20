from Hero import Hero
from Hero import Enemy
from Fight import Fight


class Dungeons:
      # karta=[["S",".","#","#",".",".",".",".",".","T"],["#","T","#","#",".",".","#","#","#,"."],
      # ["#",".","#","#","#","E","#","#","#","E"],["#",".","E",".",".",".","#","#","#","."],["#","#","#","T","#","#","#","#","#","G"]]

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        dungeon = [list(line) for line in lines]
        self.dungeon = dungeon
        self.row = 0
        self.col = 0
        self.hero = Hero()
        self.enemys = {}
        self.make_enemy_dict()

        # da napravq spisuk ot diktionarita {poziciq : Enemy}

    def get_dungeon(self):
        return self.dungeon

    def get_enemys(self):
        return self.enemys

    def print_map(self):
        new_sequence = []
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)
            new_sequence.append(ss)
        return new_sequence

    def starting_point(self, S):
        pass

    def spawn(self, hero):
        self.hero = hero

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

    def make_enemy_dict(self):
        enemys_positions = self.find_symbol("E")
        for x in enemys_positions:
            self.enemys[x] = Enemy()

# *************************************************************** mova
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
            # 
            return "You found treasure"

        if symbol == 'E':
            Fight(self.hero, self.enemys[self.row, self._col])
            return "Fight! Let the better win!"

    def make_move(self, old_positions, new_positions):
        new_row = new_positions[0]
        new_col = new_positions[1]
        old_row = old_positions[0]
        old_col = old_positions[1]
        if self.is_in_bound(new_positions):
            if self.dungeon[new_row][new_col] is not'#':
                to_return = self.return_what_found_while_moving(self.dungeon[new_row][new_col])
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
        else:
            print("Wrong input!")

# ********************************************************************* attack
    def hero_attack(self):
        # proverqvame chetirite posoki dali imame E i suotvetno go atakuvame
        # start_fight = Fight()
        pass

a = Dungeons("map.txt")
a.print_map()
a.move_hero("right")
print("               ")
a.print_map()
print("               ")
a.move_hero("right")
a.move_hero("down")
a.print_map()
