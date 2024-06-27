from abc import ABC, abstractmethod


class PlayableItem(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Song(PlayableItem):
    def __init__(self, title, artist, duration, genre, release_year):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.release_year = release_year

    def play(self):
        print(f"Playing song: {self.title} by {self.artist}")

    def display_info(self):
        print("Title:", self.title)
        print("Artist:", self.artist)
        print("Duration:", self.duration)
        print("Genre:", self.genre)
        print("Release Year:", self.release_year)
        print()


class MusicCollection(PlayableItem):
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"Added {item.title} to {self.title}.")
        else:
            print(f"Item {item.title} is already in {self.title}.")
        print()

    def play(self):
        print(f"Playing collection: {self.title}")
        for item in self.items:
            item.play()

    def display_info(self):
        print("Collection Title:", self.title)
        print("Items:")
        for item in self.items:
            item.display_info()

    def list_genres(self):
        genres = set()
        for item in self.items:
            if isinstance(item, Song):
                genres.add(item.genre)
            elif isinstance(item, MusicCollection):
                genres.update(item.list_genres())
        return list(genres)

    def play_by_genre(self, genre):
        print(f"Playing {genre} songs in collection: {self.title}")
        for item in self.items:
            if isinstance(item, Song) and item.genre == genre:
                item.play()
            elif isinstance(item, MusicCollection):
                item.play_by_genre(genre)


class Album(MusicCollection):
    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        print("Album Title:", self.title)
        print("Songs:")
        for item in self.items:
            item.display_info()


class Playlist(MusicCollection):
    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        print("Playlist Title:", self.title)
        print("Songs:")
        for item in self.items:
            item.display_info()


class Music_Library:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.playlists = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f"Song {song.title} added to the library.")
        else:
            print(f"Song {song.title} is already in the library.")
        print()

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            print(f"Album {album.title} added to the library.")
        else:
            print(f"Album {album.title} is already in the library.")
        print()

    def add_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
            print(f"Playlist {playlist.title} added to the library.")
        else:
            print(f"Playlist {playlist.title} is already in the library.")
        print()

    def play(self):
        choice = input("Do you want to play albums or playlists? (Enter 'album' or 'playlist'): ").strip().lower()

        if choice == 'album':
            if not self.albums:
                print("No albums available.")
                return

            print("Available albums:")
            for i, album in enumerate(self.albums, 1):
                print(f"{i}. {album.title}")

            album_choice = int(input("Which album do you want to play? (Enter the number): ").strip()) - 1
            if album_choice < 0 or album_choice >= len(self.albums):
                print("Invalid choice.")
                return

            chosen_album = self.albums[album_choice]
            chosen_album.play()
        elif choice == 'playlist':
            if not self.playlists:
                print("No playlists available.")
                return

            print("Available playlists:")
            for i, playlist in enumerate(self.playlists, 1):
                print(f"{i}. {playlist.title}")

            playlist_choice = int(input("Which playlist do you want to play? (Enter the number): ").strip()) - 1
            if playlist_choice < 0 or playlist_choice >= len(self.playlists):
                print("Invalid choice.")
                return

            chosen_playlist = self.playlists[playlist_choice]
            genres = chosen_playlist.list_genres()
            if genres:
                print("Available genres:")
                for i, genre in enumerate(genres, 1):
                    print(f"{i}. {genre}")
                genre_choice = int(input("Which genre do you want to play? (Enter the number): ").strip()) - 1
                if genre_choice < 0 or genre_choice >= len(genres):
                    print("Invalid choice.")
                    return
                chosen_playlist.play_by_genre(genres[genre_choice])
            else:
                print("No genres available in this playlist.")
        else:
            print("Invalid choice.")



pop_songs = [
    Song("Blinding Lights", "The Weeknd", "3:20", "Pop", 2019),
    Song("Shape of You", "Ed Sheeran", "3:53", "Pop", 2017),
    Song("Thank U, Next", "Ariana Grande", "3:27", "Pop", 2018),
    Song("Levitating", "Dua Lipa", "3:23", "Pop", 2020),
    Song("Drivers License", "Olivia Rodrigo", "4:02", "Pop", 2021)
]

rock_songs = [
    Song("Do I Wanna Know?", "Arctic Monkeys", "4:23", "Rock", 2014),
    Song("The Sky Is a Neighborhood", "Foo Fighters", "4:04", "Rock", 2017),
    Song("The Man", "The Killers", "4:10", "Rock", 2017),
    Song("My Name Is Human", "Highly Suspect", "4:18", "Rock", 2016),
    Song("Trouble’s Coming", "Royal Blood", "3:48", "Rock", 2020)
]

jazz_songs = [
    Song("Stretch Music", "Christian Scott aTunde Adjuah", "7:46", "Jazz", 2015),
    Song("Here and Now", "Veronica Swift", "5:14", "Jazz", 2019),
    Song("Dance of Shiva", "Kamasi Washington", "7:41", "Jazz", 2018),
    Song("Blow", "Theo Croker", "3:49", "Jazz", 2019),
    Song("Garden Dog Barbecue", "Snarky Puppy", "6:42", "Jazz", 2014)
]

soft_rock_songs = [
    Song("You’re Somebody Else", "Flora Cash", "3:59", "Soft Rock", 2017),
    Song("Someone You Loved", "Lewis Capaldi", "3:02", "Soft Rock", 2018),
    Song("Let It Go", "James Bay", "4:21", "Soft Rock", 2014),
    Song("Shotgun", "George Ezra", "3:21", "Soft Rock", 2018),
    Song("Call It Dreaming", "Iron & Wine", "3:56", "Soft Rock", 2017)
]

pop_album = Album("Pop Hits")
for song in pop_songs:
    pop_album.add_item(song)

rock_album = Album("Rock Hits")
for song in rock_songs:
    rock_album.add_item(song)

jazz_album = Album("Jazz Hits")
for song in jazz_songs:
    jazz_album.add_item(song)

soft_rock_album = Album("Soft Rock Hits")
for song in soft_rock_songs:
    soft_rock_album.add_item(song)


mixed_playlist = Playlist("Mixed Playlist")
mixed_playlist.add_item(pop_songs[0])
mixed_playlist.add_item(pop_songs[1])
mixed_playlist.add_item(pop_songs[3])
mixed_playlist.add_item(rock_songs[1])
mixed_playlist.add_item(rock_songs[3])
mixed_playlist.add_item(rock_songs[4])
mixed_playlist.add_item(jazz_songs[2])
mixed_playlist.add_item(jazz_songs[0])
mixed_playlist.add_item(soft_rock_songs[0])
mixed_playlist.add_item(soft_rock_songs[1])
mixed_playlist.add_item(soft_rock_songs[4])

summer_mood = Playlist("Summer Mood")
summer_mood.add_item(pop_songs[2])
summer_mood.add_item(pop_songs[4])
summer_mood.add_item(pop_songs[3])
summer_mood.add_item(rock_songs[2])
summer_mood.add_item(rock_songs[0])
summer_mood.add_item(rock_songs[3])
summer_mood.add_item(jazz_songs[1])
summer_mood.add_item(jazz_songs[3])
summer_mood.add_item(jazz_songs[0])
summer_mood.add_item(soft_rock_songs[2])
summer_mood.add_item(soft_rock_songs[3])
summer_mood.add_item(soft_rock_songs[4])


library = Music_Library()
for song in pop_songs + rock_songs + jazz_songs + soft_rock_songs:
    library.add_song(song)

library.add_album(pop_album)
library.add_album(rock_album)
library.add_album(jazz_album)
library.add_album(soft_rock_album)
library.add_playlist(mixed_playlist)
library.add_playlist(summer_mood)

library.play()