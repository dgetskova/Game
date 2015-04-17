import unittest
from hero import Hero


class GameTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Didka", title="Dragonslayer", health=10, mana=10, mana_regeneration_rate=2)

    def test_known_as_hero(self):
        self.assertEquals(self.hero.known_as(), "Didka the Dragonslayer")

if __name__ == '__main__':
    unittest.main()
