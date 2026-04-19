from user import User
from userRepository import UserRepository

user_obj=User("Python",6,"python@gmail.com")
user_repo=UserRepository("userDB","superuser","root")

user_obj.getUserInfo()
user_repo.save_to_database(user_obj)

if(user_obj.adult()):
    print("Adult")
else:print("Not Adult")