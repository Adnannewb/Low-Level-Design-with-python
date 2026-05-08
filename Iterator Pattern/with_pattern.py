from typing import List
from abc import ABC,abstractmethod


class Song:
    def __init__(self,tittle:str):
        self.__song:str=tittle
        
    def get_song(self):
        return self.__song

class Iterator(ABC):
    @abstractmethod
    def has_next(self)->bool:
        pass
    @abstractmethod
    def next_song(self):
        pass

#incase if i use any other collection like list , linkedlist ,set 
#all i need to do is this that should also inherit iterator and must have 
#hasnext and nextsong method  in that , code will be changed but the client doesn't have to do anything  

class PlaylistIterator(Iterator):
    def __init__(self,songlist:List[Song]):
        self.__songlist=songlist
        self.__position=0
    def has_next(self):
        if(self.__position < len(self.__songlist)):
            return True
        else:return False
    
    def next_song(self)->Song|None:
        while(self.has_next()==True):
            song=self.__songlist[self.__position]
            self.__position+=1
            return song
        return None
    
class Playlist:
    def __init__(self):
        self.__playlist:List[Song]=[]
        
    def add_song(self,song:Song):
        self.__playlist.append(song)
    def create_iterator(self):
        return PlaylistIterator(self.__playlist)

play=Playlist()
play.add_song(Song("song1"))
play.add_song(Song("song2"))
play.add_song(Song("song3"))
play.add_song(Song("song4"))

iterator=play.create_iterator()

while (iterator.has_next()):
    print(iterator.next_song().get_song())



    
