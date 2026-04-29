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
class AddOnDecorator(Beverage):
    def __init__(self,coffee:Coffee):
        self._coffee=coffee
        
    def description(self):
        pass
    
    def get_cost(self):
        pass
class MilkDecorator(AddOnDecorator):
    def description(self):
        return self._coffee.description()+" with"+" Milk"
    
    def get_cost(self):
        return self._coffee.get_cost()+10
class WhipCreamDecorator(AddOnDecorator):
    def description(self):
        return self._coffee.description()+" with"+" Whip Cream"
    
    def get_cost(self):
        return self._coffee.get_cost()+20

c=Coffee()
print(c.description())
print(c.get_cost())

milk=MilkDecorator(c)
print(milk.description())    
print(milk.get_cost())  

cream=WhipCreamDecorator(milk)
print(cream.description())  
print(cream.get_cost())  