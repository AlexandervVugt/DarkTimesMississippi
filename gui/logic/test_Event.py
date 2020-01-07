import unittest
import Event as Event

class EventTest(unittest.TestCase):
    def setUp(self):
        self.event = Event.Event("test", None, None, "This is a test event.")

    def test_toString(self):
        expected = "This is a test event."
        self.assertEqual(expected, self.event.toString())

    def test_equals_illegalInstance(self):
        self.assertFalse(self.event.equals("Helllo World!"))

    def test_equals_false(self):
        other = Event.Event("test1", "a", "b", "test1")
        self.assertFalse(self.event.equals(other))

    def test_equals_true(self):
        other = Event.Event("test", None, None, "This is a test event.")
        self.assertTrue(self.event.equals(other))

    def test_equals_self(self):
        self.assertTrue(self.event.equals(self.event))

if __name__ == "__main__":
    unittest.main()