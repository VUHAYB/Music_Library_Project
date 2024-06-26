from abc import ABC, abstractmethod

class Playable_Item(ABC):

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class Song(Playable_Item):

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

class Music_Collection(Playable_Item):

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

class Album(Music_Collection):

    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        print("Album Title:", self.title)
        print("Songs:")
        for item in self.items:
            item.display_info()

class Playlist(Music_Collection):

    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        print("Playlist Title:", self.title)
        print("Songs:")
        for item in self.items:
            item.display_info()


song1 = Song("We don't talk anymore", "Charlie Puth ft. Selena Gomez", "3:37", "Pop", 2015)
song2 = Song("That's my name", "Akcent", "4:06", "Dance-pop, house", 2009)
song3 = Song("Believer", "Imagine Dragons", "3:24", "Arena Rock", 2016)
song4 = Song("Levitating", "Dua Lipa", "3:23", "Pop-funk", 2020)

album = Album("English Hit Songs")
album.add_item(song1)
album.add_item(song2)
album.add_item(song4)

playlist = Playlist("Summer Mood")
playlist.add_item(song1)
playlist.add_item(song2)
playlist.add_item(song3)
playlist.add_item(album)

playlist.display_info()
playlist.play()
