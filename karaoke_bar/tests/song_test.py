import unittest

from src.song import Song
from src.room import Room


class TestSong(unittest.TestCase):
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
        


    def test_song_name(self):
        self.assertEqual("Don't stop believing", self.song1.name)

    def test_song_number(self):
        self.assertEqual(0, self.song1.number)

