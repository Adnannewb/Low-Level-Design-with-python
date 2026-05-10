from math import sqrt

class Location:
    def __init__(self,lat:float,long:float):
        self.__lat=lat
        self.__long=long
    def get_lattitue(self):
        return self.__lat
    def get_longitude(self):
        return self.__long
    def calc_distance(self,loc:'Location'):
        #Euclidean distance
        dx=self.get_lattitue()-loc.get_lattitue()
        dy=self.get_longitude()-loc.get_longitude()
        return sqrt(dx*dx+dy*dy)
        