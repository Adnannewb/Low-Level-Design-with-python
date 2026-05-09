class Airplane:
    def __init__(self,flight_number:str):
        self.__flight_number=flight_number
    def get_flight_number(self)->str:
        return self.__flight_number
    
    def send_message(self,msg:str,airplane:'Airplane'):
        print(f"{self.__flight_number} is sending message: {msg} to {airplane.get_flight_number()}")
        
spacejet=Airplane("Jet-123")
biman=Airplane("Bim-4567")
emirates=Airplane("Emi-9898")
spacejet.send_message("Taking Off",biman)
spacejet.send_message("Heading North",emirates)

#sending message to eachother occurs n^2 combination .
# creating object this much time consuming and errorful
