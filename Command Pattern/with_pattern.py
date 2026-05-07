from abc import ABC,abstractmethod
class Chef:
    def cook_pasta(self):
        print("Chef is cooking Pasta")
    def cook_pizza(self):
        print("Chef is cooking Pizza")
    def cook_Burger(self):
        print("Chef is cooking Burger")


class CommandOrder(ABC):
    @abstractmethod
    def execute_order(self):
        pass
class PizzaOrder(CommandOrder):
    def __init__(self,chef:Chef):
        self.chef=chef
    
    def execute_order(self):
        self.chef.cook_pizza()

class PastaOrder(CommandOrder):
    def __init__(self,chef:Chef):
        self.chef=chef
    
    def execute_order(self):
        self.chef.cook_pasta()
class BurgerOrder(CommandOrder):
    def __init__(self,chef:Chef):
        self.chef=chef
    
    def execute_order(self):
        self.chef.cook_Burger()



class Waiter:    
    def place_order(self,order:CommandOrder):
        order.execute_order()

chef=Chef()       
pizza=PizzaOrder(chef)
pasta=PastaOrder(chef)
burger=BurgerOrder(chef)

waiter=Waiter()
waiter.place_order(pizza)
waiter.place_order(burger)