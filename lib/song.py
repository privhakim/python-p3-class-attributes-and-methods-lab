class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.genre_count[cls] = cls.genre_count.get(cls, 0) + 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0)

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0)

# Creating song instances
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
another_song = Song("Another Song", "Artist B", "Rock")
yet_another_song = Song("Yet Another Song", "Artist C", "Country")

# Calling class methods to populate counts
Song.add_to_genre_count()
Song.add_to_artist_count()

# print
print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
