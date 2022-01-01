from tkinter import *
from ab3 import scatterGraphFunc
root = Tk(className="Python Rainfall Graphs")
def onButtonClick():
    scatterGraphFunc()

functionButton = Button(root,text="Click for graph",command=onButtonClick).pack()
root.geometry("600x400")
root.mainloop()

