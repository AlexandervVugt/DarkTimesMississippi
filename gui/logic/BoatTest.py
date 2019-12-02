import unittest
import Boat as Boat

class BoatTest(unittest.TestCase):
    def setUp(self):
        """Sets up the test case"""
        global boat

        boat = Boat.Boat(5)

    def test_load_negative(self):
        self.assertTrue(boat.load(-2))
        self.assertEqual(boat.getLoad(), 3)

    def test_load_zero(self):
        self.assertTrue(boat.load(0))
        self.assertEqual(boat.getLoad(), 5)

    def test_load_in(self):
        self.assertTrue(boat.load(5))
        self.assertEqual(boat.getLoad(), 10)

    def test_load_out(self):
        self.assertFalse(boat.load(6))
        self.assertEqual(boat.getLoad(), 5)

    def test_unload_negative(self):
        boat.unload(-3)
        self.assertEqual(boat.getLoad(), 8)
    
    def test_unload_zero(self):
        boat.unload(0)
        self.assertEqual(boat.getLoad(), 5)

    def test_unload_in(self):
        boat.unload(5)
        self.assertEqual(boat.getLoad(), 0)

    def test_unload_out(self):
        boat.unload(6)
        self.assertEqual(boat.getLoad(), 0)

    def test_equals_wrongInstance(self):
        instance = list()
        self.assertFalse(boat.equals(instance))

    def test_equals_wrongValues(self):
        instance = Boat.Boat(load = 6, capacity = 15, sellPrice = 5)
        self.assertFalse(boat.equals(instance))

    def test_equals_true(self):
        instance = Boat.Boat()
        ret = boat.equals(instance)
        self.assertTrue(ret)

    def test_equals_self(self):
        self.assertTrue(boat.equals(boat))

    def test_toString(self):
        expected = "Boat:\n\tCapacity: 10\n\tLoad: 5\n\tSell price: 2"
        self.assertEqual(boat.toString(), expected)

if __name__ == '__main__':
    unittest.main()