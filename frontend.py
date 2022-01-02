from tkinter import *
from backend import *
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter.font as font

root = Tk()
root.title("Pakistan's Rain-Temp Data ")

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

def textbuttonClick():

    def openFile():        
       tf = open("dataset/statstext.txt", 'r')
       data = tf.read()
       txtarea.insert(END, data)
       tf.close()
    
    ws = Tk()
    ws.title("Statistics")
    ws.geometry("600x450")
    ws['bg']='#fb0'

    txtarea = Text(ws, width=70, height=22)
    txtarea.pack(pady=20)

    Button(ws,text="Calculate & Show Stats",command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)
    ws.mainloop()

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

def OnHoverText(event):
    TextButton.config(bg='black', fg='white')

def OnLeaveText(event):
    TextButton.config(bg='green', fg='black')

backgroundImage = Image.open("images/Background.jpg")
resizedBackground = backgroundImage.resize((1920,1080),Image.ANTIALIAS)
newBackground = ImageTk.PhotoImage(resizedBackground)
backgroundLabel = Label( root, image =newBackground)
backgroundLabel.place(x = 0, y = 0)

tempBarButton = Button(root,text="Temp Bar Graph",width=42,height=2,command=tempBarButtonClick, bg='green', relief='groove')
tempBarButton.bind('<Enter>', OnHoverBarRain)
tempBarButton.bind('<Leave>', OnLeaveBarRain)
tempBarButton['font'] = myFont
tempBarButton.place(x=620, y= 250)

rainBarButton = Button(root,text="Rain Bar Graph",width=42,height=2,command=rainBarButtonClick, bg='green', relief='groove')
rainBarButton.bind('<Leave>', OnLeaveBarTemp)
rainBarButton.bind('<Enter>', OnHoverBarTemp)
rainBarButton['font'] = myFont
rainBarButton.place(x=620, y= 310)

multiBarButton = Button(root,text="Multi Bar Graph",width=42,height=2,command=multiBarButtonClick, bg='green', relief='groove')
multiBarButton.bind('<Enter>', OnHoverMultiBar)
multiBarButton.bind('<Leave>', OnLeaveMultiBar)
multiBarButton['font'] = myFont
multiBarButton.place(x=620, y= 370)

scatterTempButton = Button(root,text="Temp Line Plot",width=42,height=2,command=scatterTempButtonClick, bg='green', relief='groove')
scatterTempButton.bind('<Enter>', OnHoverTempScatter)
scatterTempButton.bind('<Leave>', OnLeaveTempScatter)
scatterTempButton['font'] = myFont
scatterTempButton.place(x=620, y= 430)

scatterRainButton = Button(root,text="Rain Line Plot",width=42,height=2,command=scatterRainButtonClick, bg='green', relief='groove')
scatterRainButton.bind('<Enter>', OnHoverRainScatter)
scatterRainButton.bind('<Leave>', OnLeaveRainScatter)
scatterRainButton['font'] = myFont
scatterRainButton.place(x=620, y= 490)

scatterButton = Button(root,text="Scatter Plot",width=42,height=2,command=scatterMultiButtonClick, bg='green', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton['font'] = myFont
scatterButton.place(x=620, y= 550)

boxPlotButton = Button(root,text="Box Plot",width=42,height=2,command=boxPlotButtonClick, bg='green', relief='groove')
boxPlotButton.bind('<Enter>', OnHoverBoxPlot)
boxPlotButton.bind('<Leave>', OnLeaveBoxPlot)
boxPlotButton['font'] = myFont
boxPlotButton.place(x=620, y= 610)

TextButton = Button(root,text="Text Stats",width=42,height=2,command=textbuttonClick, bg='green', relief='groove')
TextButton.bind('<Enter>', OnHoverText)
TextButton.bind('<Leave>', OnLeaveText)
TextButton['font'] = myFont
TextButton.place(x=620, y= 670)

root.state('zoomed')
root.mainloop()