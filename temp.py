from tkinter import *



def _on_click(self, event):
    text.tag_remove("highlight", "1.0", "end")
    text.tag_add("highlight", "insert wordstart", "insert wordend")

root = Tk()
root.geometry('500x200')



text = Text(root)

text.tag_config("a", foreground="blue", underline=1)
text.tag_bind("Enter>", _on_click)
text.tag_configure("highlight", background="green", foreground="black")
##text.tag_bind("Leave>", show_arrow_cursor)
##text.tag_bind("Button-1>", click)
text.config(cursor="arrow")

text.insert(INSERT, "click here!", "a")
text.place(x=50, y=100, width=400, height=20)
