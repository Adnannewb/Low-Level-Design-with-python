class Laptop:
    def __init__(self,processor:str,ram:str,display_size:str=None,color:str=None,graphic_card:str=None):
        self.processor=processor
        self.ram=ram
        self.display_size=display_size
        self.color=color
        self.graphic_card=graphic_card
    
    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"Ram: {self.ram}GB")
        if self.display_size:
            print(f"Display Size: {self.display_size}")
        if self.color:
            print(f"Color: {self.color}")
        if self.graphic_card:
            print(f"Graphic Card: {self.graphic_card}")
        
        
l=Laptop("Ryzen 7","16")
l.display_specs()

l1=Laptop("Ryzen 7","16",None,"Black",None)
l1.display_specs()