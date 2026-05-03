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


class ApiGateway:
    def __init__(self):
        self.__user_service=UserService()
        self.__order_service=OrderService()
    
    def login_user(self,username,password):
        self.__user_service.login(username,password)
    def get_user_profile(self,userid):
        self.__user_service.get_profile(userid)
    def get_order(self,userid):
        self.__order_service.get_orders(userid)
    def get_all(self,userid,username,password):
        self.__user_service.login(username,password)
        self.__user_service.get_profile(userid)
        print(self.__order_service.get_orders(userid))

api_gateway=ApiGateway()

# api_gateway.login_user("Admin","123")
# api_gateway.get_user_profile("U123")
# api_gateway.get_order("U123")

#instead of calling these three individually ,we can call all of them at a same time 
#that is something helpful  the facade pattern provides
api_gateway.get_all("U123","Admin","123")
