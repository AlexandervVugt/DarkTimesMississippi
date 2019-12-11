import unittest
import Player as Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player.Player("Tester")
    
    def test_mutateGold_negative_typical(self):
        self.assertTrue(self.player.mutateGold(-1))
        self.assertEqual(self.player.getGold(), 2)
    
    def test_mutateGold_positive_typical(self):
        self.assertTrue(self.player.mutateGold(5))
        self.assertEqual(self.player.getGold(), 8)

    def test_mutateGold_negative_out(self):
        self.assertFalse(self.player.mutateGold(-4))
        self.assertEqual(self.player.getGold(), 3)

    def test_mutateGold_negative_in(self):
        self.assertTrue(self.player.mutateGold(-3))
        self.assertEqual(self.player.getGold(), 0)

    def test_mutateWheat_negative_typical(self):
        self.assertTrue(self.player.mutateWheat(-2))
        self.assertEqual(self.player.getWheat(), 8)
    
    def test_mutateWheat_positive_typical(self):
        self.assertTrue(self.player.mutateWheat(5))
        self.assertEqual(self.player.getWheat(), 15)

    def test_mutateWheat_negative_out(self):
        self.assertFalse(self.player.mutateWheat(-11))
        self.assertEqual(self.player.getWheat(), 10)

    def test_mutateWheat_negative_in(self):
        self.assertTrue(self.player.mutateWheat(-10))
        self.assertEqual(self.player.getWheat(), 0)

    def test_destroyBoat(self):
        self.player.destroyBoat()
        self.assertFalse(self.player.hasBoat())

    def test_assignBoat_hasBoat(self):
        self.assertFalse(self.player.assignBoat())

    def test_assignBoat(self):
        self.player.destroyBoat()
        self.assertTrue(self.player.assignBoat())

    def test_assignBoat_default_multiplePlayersNewBoats(self):
        #assign
        player = Player.Player("Subject")
        player.destroyBoat()
        self.player.destroyBoat()
        player.assignBoat()
        self.player.assignBoat()

        #act
        player.getBoat().load(1)

        #assert
        self.assertEqual(self.player.getBoat().getLoad(), 0)

    def test_multiplePlayersMemoryTest(self):
        #assign
        player = Player.Player("Subject")
        
        #act
        player.getBoat().load(2)

        #assert
        self.assertEqual(self.player.getBoat().getLoad(), 0)

    def test_sellNonExistingBoat(self):
        self.player.destroyBoat()
        with self.assertRaises(AttributeError):
            self.player.sellBoat()

    def test_sellBoat(self):
        self.player.sellBoat()
        self.assertEqual(self.player.getGold(), 5)
        self.assertFalse(self.player.hasBoat())

    def test_toString(self):
        expected = "Player: Tester\n\tGold: 3\n\tWheat: 10\n\tBoat:\n\tCapacity: 10\n\tLoad: 0\n\tSell price: 2"
        self.assertEqual(self.player.toString(), expected)

    def test_equals_typeFail(self):
        self.assertFalse(self.player.equals("Hello World!"))

    def test_equals_false(self):
        other = Player.Player("Player", 9, 4)
        self.assertFalse(self.player.equals(other))

    def test_equals_self(self):
        self.assertTrue(self.player.equals(self.player))

    def test_equals_true(self):
        other = Player.Player("Tester")
        self.assertTrue(self.player.equals(other))

if __name__ == "__main__":
    unittest.main()