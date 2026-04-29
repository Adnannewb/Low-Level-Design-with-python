from typing import List
from abc import ABC,abstractmethod
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self,name:str):
        self.name=name
    def show_details(self):
        return f"File: {self.name}"

class Folder(FileSystemComponent):
    def __init__(self,name:str):
        self.name=name
        self.components:List[FileSystemComponent]=[]
    
    def add_component(self,component:FileSystemComponent):  
        self.components.append(component)   
    
    def show_details(self):
        print(f"Folder name: {self.name}")
        for component in self.components:
            print(component.show_details())
 
file1=File("Image.png")           
file2=File("ppt")           
file3=File("word.docs")

sub_folder=Folder("Sub Folder")
sub_folder.add_component(file1)           
sub_folder.add_component(file2)           
sub_folder.add_component(file3)

main_folder=Folder("Main Folder")

movie=File("With Love")
anime=File("Naruto")

main_folder.add_component(movie)
main_folder.add_component(anime)
main_folder.add_component(sub_folder)

main_folder.show_details()          
        