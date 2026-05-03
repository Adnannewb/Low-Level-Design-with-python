class UserService:
    def login(self,username:str,password:str) ->dict:
        print(f"[UserService] Logging in {username}")
        return {"userid":"U123","name":username}
    def get_profile(self,userid:str)->dict:
        print(f"[UserService] getting profile for {userid}")
        return{"userid":userid,"name":"Rahul","address":"Mumbai"}

class OrderService:
    def get_orders(self,user_id:str)->list:
        print(f"[OrderService] getting order for {user_id}")
        return[
            {"Order id":"ord-1","Total":"1500"},
            {"Order id":"ord-2","Total":"2500"}
        ]
        
user_service=UserService()
order_service=OrderService()

user_service.login("admin","1234")
user_service.get_profile("admin1")

#in that code client has all the knowledge of backend and even something change to backend 
# side need to change in client side .In that time facade pattern works ,we create middleware
# something like api gateway that will interact with client and service 

print(order_service.get_orders("admin1"))
        