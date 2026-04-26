class Logger:
    __instance=None
    def __new__(cls,file_name:str):
        if(cls.__instance==None):
            cls.__instance=super().__new__(cls)
            cls.__instance.file_name=file_name
            cls.__instance.log_count=0
            return cls.__instance
        else:return cls.__instance
    def log(self,text:str):
        print(f"Logger is logging . {text} in {self.file_name}")
        self.log_count+=1


l1=Logger("log.file")
l2=Logger("log.file")
l3=Logger("log.file")

#staff
l1.log("staff is doing his work")
#bank
l2.log("doing transactions")
#contact
l3.log("finding contact")

print(l1.log_count)
print(l2.log_count)
print(l3.log_count)
#both memory address and log count of every object are same 
print(id(l1))
print(id(l2))
print(id(l3))