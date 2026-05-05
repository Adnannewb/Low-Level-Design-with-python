from text_memento import TextMemento
class TextEditor:
    def __init__(self):
        self.__text=""
    
    def write(self,new_text):
        self.__text+=new_text
    def get_text(self):
        return self.__text
    def save(self)->TextMemento:
        return TextMemento(self.__text)    
    def restore(self,tm):
        if isinstance(tm, TextMemento):
            self.__text=tm.get_memento_text()
        else:
            self.__text=str(tm)
        