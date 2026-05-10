from location import Location
from vehicle import Vehicle
from driver import Driver
from passanger import Passenger
from ride_matching_service import RideMatchingService
from car import Car
from bike import Bike
from fare_strategy import LuxuryFareStrategy

loc1=Location(15.3243,81.2312)
loc2=Location(16.3243,82.8212)
loc3=Location(15.9843,82.9012)

car=Car("KA-2342")
bike=Bike("SHA-2342")

driver1=Driver("Jasim","jasim@gmail.com",loc2,car)
driver2=Driver("Ratul","ratul@gmail.com",loc1,bike)

passenger1=Passenger("Shihab","shihab@gmail.com",loc2)
passenger2=Passenger("Xoxo","xoxo@gmail.com",loc3)

ride_matching_service=RideMatchingService()
ride_matching_service.add_driver(driver1)
ride_matching_service.add_driver(driver2)

ride_matching_service.request_ride(passenger1,50,LuxuryFareStrategy())


