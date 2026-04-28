class Laptop:
    ram=None
    processor=None
    display_size=None
    color=None
    graphic_card=None
    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"Ram: {self.ram}GB")
        if self.display_size:
            print(f"Display Size: {self.display_size}")
        if self.color:
            print(f"Color: {self.color}")
        if self.graphic_card:
            print(f"Graphic Card: {self.graphic_card}")

class LaptopBuilder:
    def __init__(self):
        self.__laptop=Laptop()
    
    def set_processor(self,processor:str):
        self.__laptop.processor=processor
        return self
    def set_ram(self,ram:str):
        self.__laptop.ram=ram
        return self
    def set_display_size(self,display_size:str):
        self.__laptop.display_size=display_size
        return self
    def set_color(self,color:str):
        self.__laptop.color=color
        return self
    def set_graphic_card(self,graphic_card:str=None):
        self.__laptop.graphic_card=graphic_card
        return self
    
    def build(self):
        return self.__laptop

l=LaptopBuilder().set_processor("Ryzen 7").set_ram("8").set_display_size("15.6 Inches").set_color("Navy Blue").set_graphic_card(None).build()
l.display_specs()