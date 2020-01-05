import unittest
import Turn as Turn

class TurnTest(unittest.TestCase):
    def setUp(self):
        self.turn = Turn.Turn()

    def test_initiation(self):
        self.assertEqual(self.turn.getSteps(), -1)

    def test_setsteps(self):
        self.turn.setSteps(5)
        self.assertEqual(self.turn.getSteps(), 5)

if __name__ == "__main__":
    unittest.main()