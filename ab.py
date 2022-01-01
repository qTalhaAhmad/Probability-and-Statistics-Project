from tkinter import *
from ab3 import scatterGraphFunc
root = Tk(className="Python Rainfall Graphs")
def scatterButtonClick():
    scatterGraphFunc()
backgroundImage = PhotoImage(file="Background.png")
backgroundLabel = Label( root, image = backgroundImage)
backgroundLabel.place(x = 0,y = 0)
scatterButton = Button(root,text="Click for Scatter Graph",command=scatterButtonClick).pack()
root.geometry("600x400")
root.mainloop()

