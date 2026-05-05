from history import History
from text_editor import TextEditor
from text_memento import TextMemento

text_editor=TextEditor()
history=History()

text_editor.write("Hello")
text_editor.write("World")
history.save_state(text_editor.save())
# history.get_history()
text_editor.write("Good")
text_editor.write("Bye")
history.save_state(text_editor.save())
history.get_history()
print("-------------------")
re=history.undo().get_memento_text()
print(re)
history.get_history()
text_editor.restore(re)
print(text_editor.get_text())