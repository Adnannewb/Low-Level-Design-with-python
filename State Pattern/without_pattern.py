from enum import Enum

class TransportMode(Enum):
    WALKING="walking"
    BIKE="bike"
class TransportService:
    def __init__(self,transport_mode:TransportMode):
        self.__transport_mode=transport_mode
      
    def set_transport_service(self,new_transport_mode:TransportMode):
        self.__transport_mode=new_transport_mode 
        
    def eta(self):
        if(self.__transport_mode==TransportMode.WALKING):
            print("It will take 15 minutes")
        elif(self.__transport_mode==TransportMode.BIKE):
            print("It will take 5 minutes")
    def directions(self):
        if(self.__transport_mode==TransportMode.WALKING):
            print("go left and straight")
        elif(self.__transport_mode==TransportMode.BIKE):
            print("go straight")

transport_service=TransportService(TransportMode.WALKING)
transport_service.eta()
transport_service.directions()
        
#multiple If-else conditions
#violates OCP principle      
    