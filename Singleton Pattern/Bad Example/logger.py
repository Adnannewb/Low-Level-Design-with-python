class Logger:
    def __init__(self,file_name:str):
        self.file_name=file_name
        self.log_count=0
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
#log count should have been 3 because it is the same logger . But the object is created three time 
#violates the singleton pattern rule 
print(id(l1))
print(id(l2))
print(id(l3))
        