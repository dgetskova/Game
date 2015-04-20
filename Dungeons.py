class Dungeons:
      # karta=[["S",".","#","#",".",".",".",".",".","T"],["#","T","#","#",".",".","#","#","#,"."],
      # ["#",".","#","#","#","E","#","#","#","E"],["#",".","E",".",".",".","#","#","#","."],["#","#","#","T","#","#","#","#","#","G"]]

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        dungeon = [list(line) for line in lines]
        self.dungeon = dungeon

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def starting_point(self, S):
        pass

    def spawn(self, hero):
        self.hero = hero
        spawning_point=1

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
    def move_hero(self,directions)
        self.directions=directions
        directions=["right","left","up","down"]
a = Dungeons("map.txt")
a.print_map()
