class PhoneDisplay:
    def update_temperature(self,new_temp):
        print(f"Phone Display Temperature: {new_temp}")
class TVDisplay:
    def update_temperature(self,new_temp):
        print(f"TV Display Temperature: {new_temp}")
    

class WeatherStation:
    def __init__(self):
        self.__temperature=0
        self.__phone_display=PhoneDisplay()
        self.__tv_display=TVDisplay()
    
    def update_display(self,new_temp):
        self.__temperature=new_temp
        self.show_display()
        
    def show_display(self):
        self.__phone_display.update_temperature(self.__temperature)
        self.__tv_display.update_temperature(self.__temperature)

ws=WeatherStation()
ws.update_display(30)
ws.update_display(20)

#this is not a good practice , it is tightly coupled , whenever new display is added 
#it had to change in the  main class and functions 
    
    