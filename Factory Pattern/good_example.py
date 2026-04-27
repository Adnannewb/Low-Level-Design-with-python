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
   
   
class FoodFactory:
    @staticmethod
    def create_factory(item):
        if( item=="pizza"):
            return Pizza()          
        elif(item=="burger"):
            return Burger()
        
        else:
            return None
        
     
class RestaurantService:
    def food_order(self,item:str):
        order=FoodFactory.create_factory(item)
        if order is None:
            print("No food is preparing")
            return None
        order.prepare()
        
#maintain OCP and it is decoupled     



rs=RestaurantService()
rs.food_order("pizza")
rs.food_order("burger")
