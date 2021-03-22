import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song1 = Song(0,"Don't stop believing")
        self.song2 = Song(1, "Sweet Caroline")
        self.song3 = Song(2, "I'm gonna be")
        self.song4 = Song(3, "Ice Ice baby")
        self.song5 = Song(4, "Old Country Road")
        self.song6 = Song(5, "Blue suede shoes")
        self.song7 = Song(6, "yeah x3")
        self.song8 = Song(7, "baby")
        songs = [self.song1, self.song2, self.song3, self.song4, self.song5, self.song6]
        new_song = [self.song8]
        
        self.guest1 = Guest("sipho", 25, 300, 1)
        
        
    def test_room_has_song_numbers(self):
        self.assertEqual(0, self.song1.number)
    def can_add_new_song(self):
        self.room.add_song(self.song8)
        self.assertEqual(8, self.song.add_song()) 
    def test_room_has_song_names(self):
        self.assertEqual("Don't stop believing", self.song1.name)    
    def test_can_check_in_rooms(self):
        self.room.check_in(self.guest1)
        self.assertEqual(1, self.room1.check_in())
    # def test_can_check_out_rooms(self):
    #     self.guest.check_in(self.guest)
    #     self.assertEqual("checked out", self.room.check_out())
   



