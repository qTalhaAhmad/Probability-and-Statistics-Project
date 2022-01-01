from tkinter import *
from ab3 import *
root = Tk(className="Rainfall Graphs Data")

def scatterButtonClick():
    scatterGraphFunc()

def barButtonClick():
    barGraphFunc()

def OnHoverScatter(event):
    scatterButton.config(bg='black', fg='white')

def OnLeaveScatter(event):
    scatterButton.config(bg='blue', fg='black')

def OnHoverBar(event):
    barButton.config(bg='black', fg='white')

def OnLeaveBar(event):
    barButton.config(bg='blue', fg='black')

backgroundImage = PhotoImage(file="Background.png")

backgroundLabel = Label( root, image = backgroundImage)
backgroundLabel.place(x = 0, y = 0)

scatterButton = Button(root,text="Click To Display Scatter Graph",command=scatterButtonClick, bg='blue', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton.place(x=75, y= 300)

barButton = Button(root,text="Click To Display Bar Graph",command=barButtonClick, bg='blue', relief='groove')
barButton.bind('<Enter>', OnHoverBar)
barButton.bind('<Leave>', OnLeaveBar)
barButton.place(x=375, y= 300)

root.geometry("600x400")
root.mainloop()

