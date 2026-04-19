class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
    def getUserInfo(self):
        print(f"name={self.name} and age= {self.age}")
    
    def adult(self):
        return self.age>=18
    
    def save_to_database(self):
        print(f"{self.name} is getting saved to the database")
    
    def delete_from_database(self):
        print(f"{self.name} is getting deleted from the database")

#this user class doing multiple task that's violated the Single Responsibility Principle 
        
        