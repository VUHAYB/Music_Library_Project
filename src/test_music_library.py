import unittest
from music_library import Song, Album, Playlist, Music_Library

class TestMusicLibrary(unittest.TestCase):

    def setUp(self):
        self.pop_song = Song("Blinding Lights", "The Weeknd", "3:20", "Pop", 2019)
        self.rock_song = Song("Do I Wanna Know?", "Arctic Monkeys", "4:23", "Rock", 2014)
        self.album = Album("Test_album")
        self.playlist = Playlist("Test_playlist")
        self.library = Music_Library()

    def test_song_creation(self):
        self.assertEqual(self.pop_song.title, "Blinding Lights")
        self.assertEqual(self.pop_song.artist, "The Weeknd")
        self.assertEqual(self.pop_song.duration, "3:20")
        self.assertEqual(self.pop_song.genre, "Pop")
        self.assertEqual(self.pop_song.release_year, 2019)

    def test_album_add_song(self):
        self.album.add_item(self.pop_song)
        self.assertIn(self.pop_song, self.album.items)

    def test_playlist_add_song(self):
        self.playlist.add_item(self.rock_song)
        self.assertIn(self.rock_song, self.playlist.items)

    def test_library_add_song(self):
        self.library.add_song(self.pop_song)
        self.assertIn(self.pop_song, self.library.songs)

    def test_library_add_album(self):
        self.library.add_album(self.album)
        self.assertIn(self.album, self.library.albums)

    def test_library_add_playlist(self):
        self.library.add_playlist(self.playlist)
        self.assertIn(self.playlist, self.library.playlists)

    def test_album_list_genres(self):
        self.album.add_item(self.pop_song)
        self.album.add_item(self.rock_song)
        genres = self.album.list_genres()
        self.assertIn("Pop", genres)
        self.assertIn("Rock", genres)

    def test_playlist_list_genres(self):
        self.playlist.add_item(self.pop_song)
        self.playlist.add_item(self.rock_song)
        genres = self.playlist.list_genres()
        self.assertIn("Pop", genres)
        self.assertIn("Rock", genres)

if __name__ == '__main__':
    unittest.main()
