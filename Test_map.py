import unittest
from Map import Dungeons


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
            self.assertEquals(dung_of_test_dung[x], like_map[x])

    def test_is_in_bound(self):
        self.assertFalse(self.test_dung.is_in_bound([-1, -2]))

    def test_is_in_bound2(self):
        self.assertFalse(self.test_dung.is_in_bound([0, -2]))

    def test_is_in_bound3(self):
        self.assertFalse(self.test_dung.is_in_bound([0, 40]))

    def test_is_in_bound_true(self):
        self.assertTrue(self.test_dung.is_in_bound([0, 2]))

    def test_find_symbol(self):
        self.assertEquals(self.test_dung.find_symbol("S"), [0, 0])

    def test_recognizing_when_step_in_wall_in_make_move(self):
        self.assertFalse(self.test_dung.make_move([0, 0], [1, 0]))

    def test_move_fight(self):
        self.assertEquals(
            self.test_dung.make_move([0, 0], [3, 2]), "Fight! Let the better win!")

    def test_move_treasur(self):
        self.assertEquals(
            self.test_dung.make_move([0, 0], [1, 1]), "You found treasure")

    def test_move_exit(self):
        self.assertEquals(self.test_dung.make_move(
            [0, 0], [4, 9]), "You are the best ^_^ End of level!")

if __name__ == '__main__':
    unittest.main()
