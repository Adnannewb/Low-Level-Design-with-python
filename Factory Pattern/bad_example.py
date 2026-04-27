from abc import ABC,abstractmethod
class Restaurant(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Restaurant):
    def prepare(self):
        print("Pizza is preparing ....")

class Burger(Restaurant):
    def prepare(self):
        print("Burger is preparing ....")
        
class RestaurantService:
    def food_order(self,item:str):
        if( item=="pizza"):
            f=Pizza()           #Tightly coupled 
        elif(item=="burger"):
            f=Burger()          #Tightly coupled 
        else:
            print("Invalid food type!")
            return None
        f.prepare()

#violates Open close Principle

rs=RestaurantService()
rs.food_order("pizza")
rs.food_order("burger")