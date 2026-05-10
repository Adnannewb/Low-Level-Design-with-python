from typing import List
from driver import Driver
from passanger import Passenger
from location import Location
from fare_strategy import FareStrategy
from ride import Ride,RideStatus

class RideMatchingService:
    def __init__(self):
        self.__available_drivers:List[Driver]=[]
    def add_driver(self,driver:Driver):
        self.__available_drivers.append(driver)
    def request_ride(self,passenger:Passenger,distance:float,strategy:FareStrategy):
        if(len(self.__available_drivers)==0):
            passenger.notify("No Available Driver")
            return
        #Nearest Driver
        nearest_driver:Driver=self.__find_nearest_driver(passenger.get_location())
        self.__available_drivers.remove(nearest_driver)
        ride:Ride=Ride(passenger,nearest_driver,distance,strategy)
        ride.calculate_fare()
        passenger.notify(f"Ride scheduled with fare Tk. {ride.get_fare()}")
        nearest_driver.notify(f"You have one new ride of Tk {ride.get_fare()}")
        ride.update_status(RideStatus.ONGOING)
        
        #After Sometime
        ride.update_status(RideStatus.COMPLETED)
        self.add_driver(nearest_driver)
        
    
    def __find_nearest_driver(self,passanger_loc:Location) ->Driver:
        assigned_driver=None
        min_distance=float("inf")
        for driver in self.__available_drivers:
            dist=driver.get_location().calc_distance(passanger_loc)
            if(dist<min_distance):
                min_distance=dist
                assigned_driver=driver
        return assigned_driver
            
        