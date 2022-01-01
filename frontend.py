from tkinter import *
from backend import *
root = Tk(className="Rainfall Graphs Data")

def tempBarButtonClick():
    avgTMBarG()    

def rainBarButtonClick():    
    avgRMBarG()

def multiBarButtonClick():    
    tempRainMultiBarChart()

def scatterButtonClick():
    scatterGraphFunc()

def OnHoverScatter(event):
    scatterButton.config(bg='black', fg='white')

def OnLeaveScatter(event):
    scatterButton.config(bg='blue', fg='black')

def OnHoverBarTemp(event):
    rainBarButton.config(bg='black', fg='white')    

def OnLeaveBarTemp(event):
    rainBarButton.config(bg='blue', fg='black')

def OnHoverBarRain(event):
    tempBarButton.config(bg='black', fg='white')

def OnLeaveBarRain(event):
    tempBarButton.config(bg='blue', fg='black')

def OnHoverMultiBar(event):
    multiBarButton.config(bg='black', fg='white')

def OnLeaveMultiBar(event):
    multiBarButton.config(bg='blue', fg='black')

backgroundImage = PhotoImage(file="images/background.png")     # update background image with some 1920x1080 pic

backgroundLabel = Label( root, image = backgroundImage)
backgroundLabel.place(x = 0, y = 0)

tempBarButton = Button(root,text="Click To Display Temp Bar Graph",command=tempBarButtonClick, bg='blue', relief='groove')
tempBarButton.bind('<Enter>', OnHoverBarRain)
tempBarButton.bind('<Leave>', OnLeaveBarRain)
tempBarButton.place(x=75, y= 300)

rainBarButton = Button(root,text="Click To DRisplay Rain Bar Graph",command=rainBarButtonClick, bg='blue', relief='groove')
rainBarButton.bind('<Leave>', OnLeaveBarTemp)
rainBarButton.bind('<Enter>', OnHoverBarTemp)
rainBarButton.place(x=375, y= 300)

multiBarButton = Button(root,text="Click To Display Multi Bar Graph",command=multiBarButtonClick, bg='blue', relief='groove')
multiBarButton.bind('<Enter>', OnHoverMultiBar)
multiBarButton.bind('<Leave>', OnLeaveMultiBar)
multiBarButton.place(x=675, y= 300)

scatterButton = Button(root,text="Click To Display Scatter Graph",command=scatterButtonClick, bg='blue', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton.place(x=975, y= 300)

root.state('zoomed') # graphs much easier to understand in fullscreen mode, also looks better.
root.mainloop()
