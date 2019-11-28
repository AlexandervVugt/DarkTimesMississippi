import unittest
import logic.Boat as Boat

class BoatTest(unittest.TestCase):
    def load_negative(self):
        self.assertEqual(boat.load(-5), True)
        self.assertEqual(boat.getLoad(), 0)
        reset()

    def load_zero(self):
        self.assertEqual(boat.load(0), True)
        self.assertEqual(boat.getLoad(), 5)
        reset()

def setup():
    """Sets up the test case"""
    global boat

    boat = Boat.Boat(5)


def reset():
    """Resets the test case"""
    global boat

    boat = Boat.Boat(5)

if __name__ == "__main__":
    setup()
    unittest.main()