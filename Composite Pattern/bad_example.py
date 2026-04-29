from typing import List
class File:
    def __init__(self,name:str):
        self.name=name
    def show_details(self):
        return f"File: {self.name}"

class Folder:
    def __init__(self,name:str):
        self.name=name
        self.files:List[File]=[]
    def add_file(self,file:File):  #in this it just handles file but inside folder there can be a folder also 
        self.files.append(file)    #which this code doesn't do and either it cannot detect between file and folder
    def show_details(self):
        print(f"Folder name: {self.name}")
        for file in self.files:
            print(file.show_details())
 
file1=File("Image.png")           
file2=File("ppt")           
file3=File("word.docs")

folder=Folder("My Folder")
folder.add_file(file1)           
folder.add_file(file2)           
folder.add_file(file3)

folder.show_details()           
        