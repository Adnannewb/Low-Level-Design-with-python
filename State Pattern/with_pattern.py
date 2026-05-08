from abc import ABC,abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass
    @abstractmethod
    def directions(self):
        pass
    
class Walking(TransportMode):
    def eta(self):
        print("It will take 15 minutes")
        
    
    def directions(self):
        print("go left and straight")
class Bike(TransportMode):
    def eta(self):
        print("It will take 5 minutes")
        
    
    def directions(self):
        print("go straight")
        

class TransportService:
    def __init__(self,mode:TransportMode):
        self.__transport_mode=mode
    def set_transport_service(self,new_transport_mode:TransportMode):
        self.__transport_mode=new_transport_mode 
    def eta(self):
        self.__transport_mode.eta()
    def directions(self):
        self.__transport_mode.directions()

walk=Walking()
bike=Bike()

transport_service=TransportService(walk)
transport_service.eta()
transport_service.directions()
print("-----------------")
transport_service.set_transport_service(bike)
transport_service.eta()
transport_service.directions()
    