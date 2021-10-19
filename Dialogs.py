"""This is a module, which includes all the  dialogs
for the RSA Encryption
"""
import tkinter as tk

prt = None


class input_something():
    global prt

    def __init__(self, parent=None, title="Encryption", msg="Write something into the box below.",
                 initial_value="Enter something here!", **kwags):
        if parent == None:
            self.window = tk.Tk()
        else:
            self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.message = tk.Label(self.window, text=msg)
        self.message.grid(column=0, row=0, columnspan=2, padx=100)
        self.integer = tk.Entry(self.window, **kwags)
        self.integer.grid(column=0, row=1, columnspan=2,
                          padx=10, sticky=tk.E+tk.W)
        self.integer.delete(0, tk.END)
        self.integer.insert(0, initial_value)
        self.ok_button = tk.Button(self.window, text="Ok", command=self.ok)
        self.ok_button.grid(column=1, row=2, padx=50,
                            pady=10, sticky=tk.E+tk.W)
        while prt == None:
            self.window.update_idletasks()
            self.window.update()

    def ok(self):
        global prt
        prt = self.integer.get()
        self.window.destroy()


def input_Int(parent=None, title="Encryption", msg="Enter a number!",
              initial_value="Type a any number in here!", **kwags):
    global prt
    input_something(parent=parent, title=title, msg=msg,
                    initial_value=initial_value, **kwags)
    a = prt
    prt = None
    return(int(a))


def input_Str(parent=None, title="Encryption", msg="Write something!",
              initial_value="Type some text in here!"):
    global prt
    input_something(parent=parent, title=title, msg=msg,
                    initial_value=initial_value)
    a = prt
    prt = None
    return(str(a))


if __name__ == "__main__":
    h = input_Int(None, "RSA", "What is your lower bound?",
                  initial_value="100")
    print(h)
