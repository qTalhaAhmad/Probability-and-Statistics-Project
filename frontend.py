from tkinter import *
from backend import *
from PIL import ImageTk,Image
import tkinter.font as font

root = Tk(className=" Pakistan's Rain-Temp Data ")

myFont = font.Font(family='Montserrat', size=10)

def tempBarButtonClick():
    avgTMBarG()

def rainBarButtonClick():
    avgRMBarG()

def multiBarButtonClick():
    tempRainMultiBarChart()

def scatterMultiButtonClick():
    scatterMultiGraphFunc()

def scatterTempButtonClick():
    scatterTempGraphFunc()

def scatterRainButtonClick():    
    scatterRainGraphFunc()

def boxPlotButtonClick():
    boxPlotTempRain()

def OnHoverScatter(event):
    scatterButton.config(bg='black', fg='white')

def OnLeaveScatter(event):
    scatterButton.config(bg='green', fg='black')

def OnHoverTempScatter(event):
    scatterTempButton.config(bg='black', fg='white')

def OnLeaveTempScatter(event):
    scatterTempButton.config(bg='green', fg='black')

def OnHoverRainScatter(event):
    scatterRainButton.config(bg='black', fg='white')

def OnLeaveRainScatter(event):
   scatterRainButton.config(bg='green', fg='black')

def OnHoverBarTemp(event):
    rainBarButton.config(bg='black', fg='white')    

def OnLeaveBarTemp(event):
    rainBarButton.config(bg='green', fg='black')

def OnHoverBarRain(event):
    tempBarButton.config(bg='black', fg='white')

def OnLeaveBarRain(event):
    tempBarButton.config(bg='green', fg='black')

def OnHoverMultiBar(event):
    multiBarButton.config(bg='black', fg='white')

def OnLeaveMultiBar(event):
    multiBarButton.config(bg='green', fg='black')

def OnHoverBoxPlot(event):
    boxPlotButton.config(bg='black', fg='white')

def OnLeaveBoxPlot(event):
    boxPlotButton.config(bg='green', fg='black')

backgroundImage = Image.open("images/Background.jpg")
resizedBackground = backgroundImage.resize((1920,1080),Image.ANTIALIAS)
newBackground = ImageTk.PhotoImage(resizedBackground)
backgroundLabel = Label( root, image =newBackground)
backgroundLabel.place(x = 0, y = 0)

tempBarButton = Button(root,text="Temp Bar Graph",width=42,height=2,command=tempBarButtonClick, bg='green', relief='groove')
tempBarButton.bind('<Enter>', OnHoverBarRain)
tempBarButton.bind('<Leave>', OnLeaveBarRain)
tempBarButton['font'] = myFont
tempBarButton.place(x=620, y= 300)

rainBarButton = Button(root,text="Rain Bar Graph",width=42,height=2,command=rainBarButtonClick, bg='green', relief='groove')
rainBarButton.bind('<Leave>', OnLeaveBarTemp)
rainBarButton.bind('<Enter>', OnHoverBarTemp)
rainBarButton['font'] = myFont
rainBarButton.place(x=620, y= 360)

multiBarButton = Button(root,text="Multi Bar Graph",width=42,height=2,command=multiBarButtonClick, bg='green', relief='groove')
multiBarButton.bind('<Enter>', OnHoverMultiBar)
multiBarButton.bind('<Leave>', OnLeaveMultiBar)
multiBarButton['font'] = myFont
multiBarButton.place(x=620, y= 420)

scatterTempButton = Button(root,text="Temp Scatter Plot",width=42,height=2,command=scatterTempButtonClick, bg='green', relief='groove')
scatterTempButton.bind('<Enter>', OnHoverTempScatter)
scatterTempButton.bind('<Leave>', OnLeaveTempScatter)
scatterTempButton['font'] = myFont
scatterTempButton.place(x=620, y= 480)

scatterRainButton = Button(root,text="Rain Scatter Plot",width=42,height=2,command=scatterRainButtonClick, bg='green', relief='groove')
scatterRainButton.bind('<Enter>', OnHoverRainScatter)
scatterRainButton.bind('<Leave>', OnLeaveRainScatter)
scatterRainButton['font'] = myFont
scatterRainButton.place(x=620, y= 540)

scatterButton = Button(root,text="Scatter Plot",width=42,height=2,command=scatterMultiButtonClick, bg='green', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton['font'] = myFont
scatterButton.place(x=620, y= 600)

boxPlotButton = Button(root,text="Box Plot",width=42,height=2,command=boxPlotButtonClick, bg='green', relief='groove')
boxPlotButton.bind('<Enter>', OnHoverBoxPlot)
boxPlotButton.bind('<Leave>', OnLeaveBoxPlot)
boxPlotButton['font'] = myFont
boxPlotButton.place(x=620, y= 660)

root.state('zoomed')
root.mainloop()