import unittest
import Game as Game

class GameTest(unittest.TestCase):
    def setUp(self):
        """Sets up the test case"""
        global game

        game = Game.Game()

if __name__ == '__main__':
    unittest.main()