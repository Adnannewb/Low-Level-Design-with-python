class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
    def getUserInfo(self):
        print(f"name= {self.name} and age= {self.age}")
    
    def adult(self):
        return self.age>=18
#this class only shows user details nothing else