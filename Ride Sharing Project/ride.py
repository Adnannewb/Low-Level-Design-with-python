from enum import Enum
from passanger import Passenger
from driver import Driver
from fare_strategy import FareStrategy

class RideStatus(Enum):
    SCHEDULED="SCHEDULED"
    ONGOING="ONGOING"
    COMPLETED="COMPLETED"

class Ride:
    def __init__(self,passenger:"Passenger",driver:"Driver",distance:float,fare_strategy:"FareStrategy"):
        self.passenger=passenger
        self.driver=driver
        self.distance=distance
        self.fare_strategy=fare_strategy
        self.fare:float=0.0
        self.status:RideStatus=RideStatus.SCHEDULED
        
    def calculate_fare(self):
        self.fare=self.fare_strategy.calc_fare(self.driver.get_vehicle(),self.distance)
    def get_fare(self):
        return self.fare
    def update_status(self,new_ride_status:RideStatus):
        self.status=new_ride_status
        self.__notify_users(self.status)
    def __notify_users(self,ride_status:RideStatus):
        self.driver.notify(f"Your ride is {ride_status.value}")
        self.passenger.notify(f"Your ride is {ride_status.value}")
        
        
        
    
 