from abc import ABC,abstractmethod
class Beverage(ABC):
    @abstractmethod
    def description(self):
        pass
    @abstractmethod
    def get_cost(self):
        pass
class Coffee(Beverage):
    def description(self):
        return "Plain Coffee"
    
    def get_cost(self):
        return 20
class CoffeeWithMilk(Beverage):
    def description(self):
        return "Coffee with milk"
    
    def get_cost(self):
        return 30 
class CoffeeWithWhipCream(Beverage):
    def description(self):
        return "Coffee with whip cream"
    
    def get_cost(self):
        return 40

c=Coffee()
print(c.description())
print(c.get_cost())

cm=CoffeeWithMilk()
print(cm.description())
print(cm.get_cost())

cc=CoffeeWithWhipCream()
print(cc.description())
print(cc.get_cost())

#for every combination i need to write specific class ,so this is a bad practice
#It's where the Decorator pattern helps 