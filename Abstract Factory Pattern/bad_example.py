from abc import ABC,abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

# North Indian Dishes

class PaneerTikka(Food):
    def prepare(self):
        print("Paneer Tikka is preparing")
class ButterChicken(Food):
    def prepare(self):
        print("Butter Chicken is preparing")
class GulabJamun(Food):
    def prepare(self):
        print("Gulab Jamun is preparing")

#South Indian Dishes
class Meduvada(Food):
    def prepare(self):
        print("Meduvada is preparing")
class Dosa(Food):
    def prepare(self):
        print("Dosa is preparing")
class Payasum(Food):
    def prepare(self):
        print("Payasum is preparing")

class RestaurantService:
    def create_meal(self,cuisine_type:str):
        if(cuisine_type=="NorthIndian"):
            starter=PaneerTikka()
            mainCourse=ButterChicken()
            dessert=GulabJamun()
        elif(cuisine_type=="Southindian"):
            starter=Meduvada()
            mainCourse=Dosa()
            dessert=Payasum()
        else:
            print("Cuisine not available")
            return None
        starter.prepare()
        mainCourse.prepare()
        dessert.prepare()

rs=RestaurantService()
rs.create_meal("Southindian")

#tightly coupled and violates OCP
