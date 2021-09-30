"""This is a module, which includes all the  dialogs
for the RSA Verschlüsselung
"""

from tkinter import Tk, Label, Entry, Button, END, mainloop, IntVar, Toplevel, mainloop


prt = None

class input_something():
    global prt
    def __init__(self, parent=None, title='Verschlüsselung', msg='Schreibe eine Zahl',
              initial_value='Tippen Sie eine Zahl ein.'):
        if parent == None:
            self.window = Tk()
        else:
            self.window = Toplevel(parent)
        self.window.title(title)
        self.window.geometry('500x200')
        self.message = Label(self.window, text=msg)
        self.message.place(x=10, y=10, width=480, height=100)
        self.integer = Entry(self.window)
        self.integer.place(x=50, y=100, width=400, height=20)
        self.integer.delete(0, END)
        self.integer.insert(0, initial_value)

        self.ok_button = Button(self.window, text='Ok', command=self.ok)
        self.ok_button.place(x = 50, y=150, width=100, height=30)
        # self.window.grab_set_global()
        while prt == None:
            self.window.update_idletasks()
            self.window.update()
        # self.window.mainloop()

    def ok(self):
        global prt
        prt = self.integer.get()
        self.window.destroy()
        
def input_Int(parent=None, title='Verschlüsselung', msg='Schreibe eine Zahl',
              initial_value='Tippen Sie eine Zahl ein.'):
    global prt
    input_something(parent=parent, title=title, msg=msg,
              initial_value=initial_value)
    a = prt
    prt = None
    return(int(a))

def input_Str(parent=None, title="Verschlüsselung", msg="Schreibe etwas!",
              initial_value="Tippen Sie etwa herein."):
    global prt
    input_something(parent=parent, title=title, msg=msg,
              initial_value=initial_value)
    a = prt
    prt = None
    return(str(a))

if __name__ == "__main__":
    # print(ord(str(1)))
    # print(chr(49))
    h = input_Int(None, 'RSA','Was ist die tiefste Zufallszahl?', initial_value='100')
    print(h)
    # print("h.prt =", h.prt)


##window = Tk()
##def test():
##    global n
##    n=0
##    a = Entry(window)
##    a.pack()
##
##
##    
##test()
##
##import os
##
##class Dialog(Toplevel):
##
##    def __init__(self, parent, title = None):
##
##        Toplevel.__init__(self, parent)
##        self.transient(parent)
##
##        if title:
##            self.title(title)
##
##        self.parent = parent
##
##        self.result = None
##
##        body = Frame(self)
##        self.initial_focus = self.body(body)
##        body.pack(padx=5, pady=5)
##
##        self.buttonbox()
##
##        self.grab_set()
##
##        if not self.initial_focus:
##            self.initial_focus = self
##
##        self.protocol("WM_DELETE_WINDOW", self.cancel)
##
##        self.geometry("+%d+%d" % (parent.winfo_windowx()+50,
##                                  parent.winfo_windowy()+50))
##
##        self.initial_focus.focus_set()
##
##        self.wait_window(self)
##
##    #
##    # construction hooks
##
##    def body(self, master):
##        # create dialog body.  return widget that should have
##        # initial focus.  this method should be overridden
##
##        pass
##
##    def buttonbox(self):
##        # add standard button box. override if you don't want the
##        # standard buttons
##
##        box = Frame(self)
##
##        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
##        w.pack(side=LEFT, padx=5, pady=5)
##        w = Button(box, text="Cancel", width=10, command=self.cancel)
##        w.pack(side=LEFT, padx=5, pady=5)
##
##        self.bind("<Return>", self.ok)
##        self.bind("<Escape>", self.cancel)
##
##        box.pack()
##
##    #
##    # standard button semantics
##
##    def ok(self, event=None):
##
##        if not self.validate():
##            self.initial_focus.focus_set() # put focus back
##            return
##
##        self.withdraw()
##        self.update_idletasks()
##
##        self.apply()
##
##        self.cancel()
##
##    def cancel(self, event=None):
##
##        # put focus back to the parent window
##        self.parent.focus_set()
##        self.destroy()
##
##    #
##    # command hooks
##
##    def validate(self):
##
##        return 1 # override
##
##    def apply(self):
##
##        pass # override
