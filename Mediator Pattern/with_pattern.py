from abc import ABC,abstractmethod
from typing import List

class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self):
        pass
    @abstractmethod
    def send_message(self):
        pass

class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes:List[Airplane]= []
        
    def register_airplane(self,new_airplane:"Airplane"):
        self.__airplanes.append(new_airplane)
        
    def send_message(self,msg:str,airplanee:"Airplane"):
        for airplane in self.__airplanes:
            if(airplanee!=airplane):
                airplane.receive_message(msg,airplanee)
            

class Airplane:
    def __init__(self,flight_number:str,tower:'ControlTower'):
        self.__flight_number=flight_number
        self.__tower=tower
        self.__tower.register_airplane(self)
        
    def get_flight_number(self):
        return self.__flight_number
    def send_message(self,msg:str):
        self.__tower.send_message(msg,self)
    
    def receive_message(self,msg:str,who_sent:'Airplane'):
        print(f"{self.__flight_number} is receiving message: {msg} from {who_sent.get_flight_number()}")

control_tower=ControlTower()
spacejet=Airplane("Jet-123",control_tower)
biman=Airplane("Bim-4567",control_tower)
emirates=Airplane("Emi-9898",control_tower)
indigo=Airplane("Ind-231",control_tower)

spacejet.send_message("Taking Off")
