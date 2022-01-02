from tkinter import *
from backend import *
from PIL import ImageTk,Image
root = Tk(className="Rainfall Graphs Data")

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
    scatterButton.config(bg='blue', fg='black')

def OnHoverTempScatter(event):
    scatterTempButton.config(bg='black', fg='white')

def OnLeaveTempScatter(event):
    scatterTempButton.config(bg='blue', fg='black')

def OnHoverRainScatter(event):
    scatterRainButton.config(bg='black', fg='white')

def OnLeaveRainScatter(event):
   scatterRainButton.config(bg='blue', fg='black')

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

def OnHoverBoxPlot(event):
    boxPlotButton.config(bg='black', fg='white')

def OnLeaveBoxPlot(event):
    boxPlotButton.config(bg='blue', fg='black')

backgroundImage = Image.open("images/Background.jpg")

resizedBackground = backgroundImage.resize((1920,1080),Image.ANTIALIAS)

newBackground = ImageTk.PhotoImage(resizedBackground)

backgroundLabel = Label( root, image =newBackground)
backgroundLabel.place(x = 0, y = 0)

tempBarButton = Button(root,text="Click To Display Temp Bar Graph",command=tempBarButtonClick, bg='blue', relief='groove')
tempBarButton.bind('<Enter>', OnHoverBarRain)
tempBarButton.bind('<Leave>', OnLeaveBarRain)
tempBarButton.place(x=75, y= 300)

rainBarButton = Button(root,text="Click To Display Rain Bar Graph",command=rainBarButtonClick, bg='blue', relief='groove')
rainBarButton.bind('<Leave>', OnLeaveBarTemp)
rainBarButton.bind('<Enter>', OnHoverBarTemp)
rainBarButton.place(x=375, y= 300)

multiBarButton = Button(root,text="Click To Display Multi Bar Graph",command=multiBarButtonClick, bg='blue', relief='groove')
multiBarButton.bind('<Enter>', OnHoverMultiBar)
multiBarButton.bind('<Leave>', OnLeaveMultiBar)
multiBarButton.place(x=675, y= 300)

scatterTempButton = Button(root,text="Click To Display Temp Scatter Graph",command=scatterTempButtonClick, bg='blue', relief='groove')
scatterTempButton.bind('<Enter>', OnHoverTempScatter)
scatterTempButton.bind('<Leave>', OnLeaveTempScatter)
scatterTempButton.place(x=75, y= 400)

scatterRainButton = Button(root,text="Click To Display Rain Scatter Graph",command=scatterRainButtonClick, bg='blue', relief='groove')
scatterRainButton.bind('<Enter>', OnHoverRainScatter)
scatterRainButton.bind('<Leave>', OnLeaveRainScatter)
scatterRainButton.place(x=375, y= 400)

scatterButton = Button(root,text="Click To Display Multi Scatter Graph",command=scatterMultiButtonClick, bg='blue', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton.place(x=675, y= 400)

boxPlotButton = Button(root,text="Click To Display Box Plot",command=boxPlotButtonClick, bg='blue', relief='groove')
boxPlotButton.bind('<Enter>', OnHoverBoxPlot)
boxPlotButton.bind('<Leave>', OnLeaveBoxPlot)
boxPlotButton.place(x=475, y= 200)

root.state('zoomed') # graphs much easier to understand in fullscreen mode, also looks better.
root.mainloop()
