from abc import ABC,abstractmethod
from typing import List

class Observer(ABC):
    def update_temperature(self,new_temp):
        pass

class PhoneDisplay(Observer):
    def update_temperature(self,new_temp):
        print(f"Phone Display Temperature: {new_temp}")
class TVDisplay(Observer):
    def update_temperature(self,new_temp):
        print(f"TV Display Temperature: {new_temp}")
    

class WeatherStation:
    def __init__(self):
        self.__temperature=0
        self.__observers:List[Observer]=[]
         
    def add_observer(self,new_observer:Observer):
        self.__observers.append(new_observer)
    
    def remove_observer(self,ob:Observer):
        self.__observers.remove(ob)
        
    def update_display(self,new_temp):
        self.__temperature=new_temp
        self.show_display()
    
        
    def show_display(self):
        for observer in self.__observers:
            observer.update_temperature(self.__temperature)
pd=PhoneDisplay()
tv=TVDisplay()
ws=WeatherStation()
ws.add_observer(pd)
ws.add_observer(tv)
# ws.remove_observer(pd)

ws.update_display(30)
ws.update_display(20)

#this is not a good practice , it is tightly coupled , whenever new display is added 
#it had to change in the  main class and functions 
    
    