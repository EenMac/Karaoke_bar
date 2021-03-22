import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("sipho", 25, 300, 1)
        self.guest2 = Guest("Jimmy", 36, 2000, 1)
        self.guest3 = Guest("Sampson", 32, 700, 1)
        self.guest4 = Guest("Micaela", 24, 400, 1)
        self.guest5 = Guest("Jessica", 27, 70, 1)
        guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5]


    def test_guest_has_name(self):
        self.assertEqual("sipho", self.guest1.name)

    def test_guest_has_dosh(self):
        self.assertEqual(300, self.guest1.dosh)

    def test_guest_age(self):
        self.assertEqual(25, self.guest1.age)
    
    # def test_wooooo(self):
    #     self.song.woooo("Don't stop believing")
    #     self.assertAlmostEqual("wooooo", self.song.name )  


        