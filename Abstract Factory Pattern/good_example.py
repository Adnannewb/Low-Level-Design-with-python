from abc import ABC,abstractmethod
class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass
class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass

# North Indian Dishes

class PaneerTikka(Starter):
    def prepare(self):
        print("Paneer Tikka is preparing")
class ButterChicken(MainCourse):
    def prepare(self):
        print("Butter Chicken is preparing")
class GulabJamun(Dessert):
    def prepare(self):
        print("Gulab Jamun is preparing")

# South Indian Dishes
class Meduvada(Starter):
    def prepare(self):
        print("Meduvada is preparing")
class Dosa(MainCourse):
    def prepare(self):
        print("Dosa is preparing")
class Payasum(Dessert):
    def prepare(self):
        print("Payasum is preparing")

class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self) -> Starter:
        pass
    @abstractmethod
    def create_mainCourse(self) -> MainCourse:
        pass
    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass

class NorthIndianCuisine(CuisineFactory):
    def create_starter(self) ->Starter:
        return PaneerTikka()
    
    def create_mainCourse(self) ->MainCourse:
        return ButterChicken()
    
    def create_dessert(self) ->Dessert:
        return GulabJamun()
class SouthIndianCuisine(CuisineFactory):
    def create_starter(self) ->Starter:
        return Meduvada()
    
    def create_mainCourse(self) ->MainCourse:
        return Dosa()
    
    def create_dessert(self) ->Dessert:
        return Payasum()
    

class RestaurantService:
    def __init__(self,factory:CuisineFactory):
        self.__factory=factory
        
    def create_meal(self):
        starter=self.__factory.create_starter()
        maincourse=self.__factory.create_mainCourse()
        dessert=self.__factory.create_dessert()
        
        starter.prepare()
        maincourse.prepare()
        dessert.prepare()

nc=NorthIndianCuisine()
rs=RestaurantService(nc)
rs.create_meal()
print()
sc=SouthIndianCuisine()
rs1=RestaurantService(sc)
rs1.create_meal()
