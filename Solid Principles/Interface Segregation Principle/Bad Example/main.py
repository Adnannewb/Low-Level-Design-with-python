from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def eat(self):
        pass
    def work(self):
        pass

class Robot(Employee):
    def work(self):
        print("Robot is working")
    def eat(self):
        raise Exception("Robot cannot eat")
worker1=Robot()
worker1.work()
worker1.eat()

#this violate Interface Segregation Principle because in robot there is 
#eat method which is not useable in that class 

    