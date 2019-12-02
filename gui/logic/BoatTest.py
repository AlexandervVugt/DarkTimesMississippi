import unittest
import Boat as Boat

class BoatTest(unittest.TestCase):
    def load_negative(self):
        self.assertTrue(boat.load(-2))
        self.assertEqual(boat.getLoad(), 3)
        reset()

    def load_zero(self):
        self.assertTrue(boat.load(0))
        self.assertEqual(boat.getLoad(), 5)
        reset()

    def load_in(self):
        self.assertTrue(boat.load(5))
        self.assertEqual(boat.getLoad(), 10)
        reset()

    def load_out(self):
        self.assertFalse(boat.load(6))
        self.assertEqual(boat.getLoad(), 5)
        reset()

    def unload_negative(self):
        boat.unload(-3)
        self.assertEqual(boat.getLoad(), 8)
        reset()
    
    def unload_zero(self):
        boat.unload(0)
        self.assertEqual(boat.getLoad(), 5)
        reset()

    def unload_in(self):
        boat.unload(5)
        self.assertEqual(boat.getLoad(), 0)
        reset()

    def unload_out(self):
        boat.unload(6)
        self.assertEqual(boat.getLoad(), 0)
        reset()

    def equals_wrongInstance(self):
        instance = list()
        self.assertFalse(boat.equals(instance))
        reset()

    def equals_wrongValues(self):
        instance = Boat.Boat(load = 6, capacity = 15, sellPrice = 5)
        self.assertFalse(boat.equals(instance))
        reset()

    def equals_true(self):
        instance = Boat.Boat()
        self.assertTrue(boat.equals(instance))
        reset()

    def equals_self(self):
        self.assertTrue(boat.equals(boat))
        reset()

    def toString_test(self):
        expected = "Boat:\n\tCapacity: 10\n\tLoad: 5\n\tSell price: 2"
        self.assertEqual(boat.toString(), expected)

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