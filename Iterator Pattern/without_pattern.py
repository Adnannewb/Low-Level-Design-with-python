from typing import List

class Song:
    def __init__(self,tittle:str):
        self.__song:str=tittle
        
    def get_song(self)->str:
        return self.__song

class Playlist:
    def __init__(self):
        self.__playlist:List[Song]=[]
    def add_song(self,song:Song):
        self.__playlist.append(song)
    def get_playlist(self):
        return self.__playlist

play=Playlist()
play.add_song(Song("song1"))
play.add_song(Song("song2"))
play.add_song(Song("song3"))
play.add_song(Song("song4"))

for i in range(len(play.get_playlist())):
    print(play.get_playlist()[i].get_song())
    
#now if i use set instead of list , it will show error 
# and client need to see the structure or code to see what collection has been used 
#Iterator design pattern solve this issues that no need to see the structure 