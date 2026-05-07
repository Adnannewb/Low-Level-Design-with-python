class Chef:
    def cook_pasta(self):
        print("Chef is cooking Pasta")
    def cook_pizza(self):
        print("Chef is cooking Pizza")
class Waiter:
    def __init__(self,chef:Chef):
        self.chef=chef
    
    def place_order(self,item:str):
        if item=="pasta":
            self.chef.cook_pasta()  
        elif item=="pozza":
            self.chef.cook_pizza()
        else:
            print("Invalid Order") 
chef=Chef()
waiter=Waiter(chef)
waiter.place_order("pasta") 

#violates ocp and tight coupling 