import unittest
import Player as Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player.Player("Tester")

if __name__ == "__main__":
    unittest.main()