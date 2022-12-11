from project.song import Song


class Album:
    def __init__(self, name, *kwargs):
        self.name = name
        # self.kwargs = kwargs
        self.published = False
        self.songs = [song for song in kwargs]
        #
        # for song in kwargs:
        #     self.songs.append(song)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."

        for song_check in self.songs:
            if song_check.name == song.name:
                return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name:str):
        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album"

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        result.strip()
        return result



# song = Song("Running in the 90s", 3.45, False)
# test_album = Album("testov", song)
# print(test_album.songs)
# song2 = Song("shushana", 3.45, False)
# test_album.add_song(song2)
# for song in test_album.songs:
#     print(song.get_info())

