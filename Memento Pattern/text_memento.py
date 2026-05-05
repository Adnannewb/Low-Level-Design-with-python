class TextMemento:
    def __init__(self,text):
        self.__saved_text=text
        
    def get_memento_text(self)->str:
        return self.__saved_text
        