from abc import ABC,abstractmethod
from vehicle import Vehicle

class FareStrategy(ABC):
    @abstractmethod
    def calc_fare(self,vehicle:'Vehicle',distance):
        pass

class StandardFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        return vehicle.get_fare()*distance

class SharedFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        return vehicle.get_fare()*distance*.5

class LuxuryFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        return vehicle.get_fare()*distance*1.5
    