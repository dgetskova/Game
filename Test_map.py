import unittest
from Map import Dungeons
from Hero import Enemy


class DungeonsTest(unittest.TestCase):

    def setUp(self):
        self.test_dung = Dungeons("map.txt")

    def test_print(self):
        like_map = []
        like_map.append(['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'])
        like_map.append(['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'])
        like_map.append(['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'])
        like_map.append(['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'])
        like_map.append(['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G'])
        dung_of_test_dung = self.test_dung.get_dungeon()
        len_line = len(like_map)
        for x in range(0, len_line):
            self.assertEqual(dung_of_test_dung[x], like_map[x])

    def test_is_in_bound(self):
        self.assertFalse(self.test_dung.is_in_bound([-1, -2]))

    def test_is_in_bound2(self):
        self.assertFalse(self.test_dung.is_in_bound([0, -2]))

    def test_is_in_bound3(self):
        self.assertFalse(self.test_dung.is_in_bound([0, 40]))

    def test_is_in_bound_true(self):
        self.assertTrue(self.test_dung.is_in_bound([0, 2]))

    def test_find_symbol_S(self):
        self.assertEqual(self.test_dung.find_symbol("S"), [(0, 0)])

    def test_find_symbol_E(self):
        self.assertEqual(self.test_dung.find_symbol("E"), [(2, 5), (2, 9), (3, 2)])

    def test_recognizing_when_step_in_wall_in_make_move(self):
        self.assertFalse(self.test_dung.make_move([0, 0], [1, 0]))

    def test_move_fight(self):
        self.assertEqual(
            self.test_dung.make_move([0, 0], [3, 2]), "Fight! Let the better win!")

    def test_move_treasur(self):
        self.assertEqual(
            self.test_dung.make_move([0, 0], [1, 1]), "You found treasure")

    def test_move_exit(self):
        self.assertEqual(self.test_dung.make_move(
            [0, 0], [4, 9]), "You are the best ^_^ End of level!")

    def test_make_enemy(self):
        enemy_dict = {}
        evil_enemy = Enemy()
        enemy_dict[(2, 5)] = evil_enemy
        enemy_dict[(2, 9)] = evil_enemy
        enemy_dict[(3, 2)] = evil_enemy
        pos = [(2, 5), (2, 9), (3, 2)]
        original_enemy = self.test_dung.get_enemys()
        print(original_enemy)
        for x in pos:
            self.assertEqual(original_enemy[x], enemy_dict[x])

if __name__ == '__main__':
    unittest.main()
