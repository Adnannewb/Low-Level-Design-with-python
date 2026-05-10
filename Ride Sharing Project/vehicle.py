from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,number_plate:str):
        self.number_plate=number_plate
    @abstractmethod
    def get_fare(self):
        pass