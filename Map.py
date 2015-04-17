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

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def starting_point(self, S):
        pass

    def spawn(self, hero):
        self.hero = hero

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

    def is_in_bound(self, positions):
        # positions = [row, col]
        count_row = len(self.dungeon)
        print(positions)
        print(type(positions))
        if positions[0] >= 0 and positions[0] < count_row:
            # tuk da si napravq izmestvaneto v kartata
            return True
        return False

    def is_valid_move(self, directions):
        if directions == "up":
            return self.is_in_bound([self.row - 1, self.col])

        elif directions == "down":
            return self.is_in_bound([self.row + 1, self.col])

        elif directions == "left":
            print("l")
        elif directions == "right":
            print("r")

    def move_hero(self, directions):
        if directions in ["up", "down", "left", "right"]:
            return self.is_valid_move(directions)
        else:
            print("Wrong input!")


a = Dungeons("map.txt")
a.print_map()
