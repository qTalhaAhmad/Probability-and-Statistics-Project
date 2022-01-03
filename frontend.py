from tkinter import *
from backend import *
from PIL import ImageTk,Image
import tkinter.font as font

root = Tk()
root.title("Pakistan's Rain-Temp Data")

myFont = font.Font(family='Montserrat', size=10)

def tempBarButtonClick():
    avgTMBarG()

def rainBarButtonClick():
    avgRMBarG()

def multiBarButtonClick():
    tempRainMultiBarChart()

def scatterTempButtonClick():
    scatterTempGraphFunc()

def scatterTempDecadeButtonClick():
    scatterTempGraphFuncDecade()

def scatterRainButtonClick():    
    scatterRainGraphFunc()

def scatterRainDecadeButtonClick():    
    scatterRainGraphFuncDecade()

def scatterMultiButtonClick():
    scatterMultiGraphFunc()

def scatterMultiDecadeButtonClick():
    scatterMultiGraphFuncDecade()

def boxPlotButtonClick():
    boxPlotTempRain()

def boxPlotDecadeButtonClick():
    boxPlotTempRainDecade()

def LRButtonClick():
    linearReg()

def LRButton2Click():
    linearReg2()

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

def OnHoverScatterDecade(event):
    scatterButtonDecade.config(bg='black', fg='white')

def OnLeaveScatterDecade(event):
    scatterButtonDecade.config(bg='green', fg='black')

def OnHoverTempScatterDecade(event):
    scatterTempButtonDecade.config(bg='black', fg='white')

def OnLeaveTempScatterDecade(event):
    scatterTempButtonDecade.config(bg='green', fg='black')

def OnHoverRainScatterDecade(event):
    scatterRainButtonDecade.config(bg='black', fg='white')

def OnLeaveRainScatterDecade(event):
   scatterRainButtonDecade.config(bg='green', fg='black')

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

def OnLeaveBoxPlotDecade(event):
    boxPlotDecadeButton.config(bg='green', fg='black')

def OnHoverBoxPlotDecade(event):
    boxPlotDecadeButton.config(bg='black', fg='white')

def OnHoverText(event):
    TextButton.config(bg='black', fg='white')

def OnLeaveText(event):
    TextButton.config(bg='green', fg='black')

def OnHoverLR(event):
    LRButton.config(bg='black', fg='white')

def OnLeaveLR(event):
    LRButton.config(bg='green', fg='black')

def OnHoverLR2(event):
    LRButton2.config(bg='black', fg='white')

def OnLeaveLR2(event):
    LRButton2.config(bg='green', fg='black')

backgroundImage = Image.open("images/Background.jpg")
resizedBackground = backgroundImage.resize((1920,1080),Image.ANTIALIAS)
newBackground = ImageTk.PhotoImage(resizedBackground)
backgroundLabel = Label( root, image =newBackground)
backgroundLabel.place(x = 0, y = 0)

multiBarButton = Button(root,text="Multi Bar Graph",width=42,height=2,command=multiBarButtonClick, bg='green', relief='groove')
multiBarButton.bind('<Enter>', OnHoverMultiBar)
multiBarButton.bind('<Leave>', OnLeaveMultiBar)
multiBarButton['font'] = myFont
multiBarButton.place(x=620, y= 260)

tempBarButton = Button(root,text="Temp Bar Graph",width=42,height=2,command=tempBarButtonClick, bg='green', relief='groove')
tempBarButton.bind('<Enter>', OnHoverBarRain)
tempBarButton.bind('<Leave>', OnLeaveBarRain)
tempBarButton['font'] = myFont
tempBarButton.place(x=420, y= 320)

rainBarButton = Button(root,text="Rain Bar Graph",width=42,height=2,command=rainBarButtonClick, bg='green', relief='groove')
rainBarButton.bind('<Leave>', OnLeaveBarTemp)
rainBarButton.bind('<Enter>', OnHoverBarTemp)
rainBarButton['font'] = myFont
rainBarButton.place(x=820, y= 320)

scatterTempButton = Button(root,text="Temp Line Plot by Month",width=42,height=2,command=scatterTempButtonClick, bg='green', relief='groove')
scatterTempButton.bind('<Enter>', OnHoverTempScatter)
scatterTempButton.bind('<Leave>', OnLeaveTempScatter)
scatterTempButton['font'] = myFont
scatterTempButton.place(x=420, y= 380)

scatterRainButton = Button(root,text="Rain Line Plot by Month",width=42,height=2,command=scatterRainButtonClick, bg='green', relief='groove')
scatterRainButton.bind('<Enter>', OnHoverRainScatter)
scatterRainButton.bind('<Leave>', OnLeaveRainScatter)
scatterRainButton['font'] = myFont
scatterRainButton.place(x=420, y= 440)

scatterButton = Button(root,text="Scatter Plot by Month",width=42,height=2,command=scatterMultiButtonClick, bg='green', relief='groove')
scatterButton.bind('<Enter>', OnHoverScatter)
scatterButton.bind('<Leave>', OnLeaveScatter)
scatterButton['font'] = myFont
scatterButton.place(x=420, y= 500)

scatterTempButtonDecade = Button(root,text="Temp Line Plot by Decade",width=42,height=2,command=scatterTempDecadeButtonClick, bg='green', relief='groove')
scatterTempButtonDecade.bind('<Enter>', OnHoverTempScatterDecade)
scatterTempButtonDecade.bind('<Leave>', OnLeaveTempScatterDecade)
scatterTempButtonDecade['font'] = myFont
scatterTempButtonDecade.place(x=820, y= 380)

scatterRainButtonDecade = Button(root,text="Rain Line Plot by Decade",width=42,height=2,command=scatterRainDecadeButtonClick, bg='green', relief='groove')
scatterRainButtonDecade.bind('<Enter>', OnHoverRainScatterDecade)
scatterRainButtonDecade.bind('<Leave>', OnLeaveRainScatterDecade)
scatterRainButtonDecade['font'] = myFont
scatterRainButtonDecade.place(x=820, y= 440)

scatterButtonDecade = Button(root,text="Scatter Plot by Decade",width=42,height=2,command=scatterMultiDecadeButtonClick, bg='green', relief='groove')
scatterButtonDecade.bind('<Enter>', OnHoverScatterDecade)
scatterButtonDecade.bind('<Leave>', OnLeaveScatterDecade)
scatterButtonDecade['font'] = myFont
scatterButtonDecade.place(x=820, y= 500)

boxPlotButton = Button(root,text="Box Plot by Month",width=42,height=2,command=boxPlotButtonClick, bg='green', relief='groove')
boxPlotButton.bind('<Enter>', OnHoverBoxPlot)
boxPlotButton.bind('<Leave>', OnLeaveBoxPlot)
boxPlotButton['font'] = myFont
boxPlotButton.place(x=420, y= 560)

boxPlotDecadeButton = Button(root,text="Box Plot by Decade",width=42,height=2,command=boxPlotDecadeButtonClick, bg='green', relief='groove')
boxPlotDecadeButton.bind('<Enter>', OnHoverBoxPlotDecade)
boxPlotDecadeButton.bind('<Leave>', OnLeaveBoxPlotDecade)
boxPlotDecadeButton['font'] = myFont
boxPlotDecadeButton.place(x=820, y= 560)

LRButton = Button(root,text="Linear Regression",width=42,height=2,command=LRButtonClick, bg='green', relief='groove')
LRButton.bind('<Enter>', OnHoverLR)
LRButton.bind('<Leave>', OnLeaveLR)
LRButton['font'] = myFont
LRButton.place(x=420, y= 620)

LRButton = Button(root,text="Linear Regression T o R",width=42,height=2,command=LRButtonClick, bg='green', relief='groove')
LRButton.bind('<Enter>', OnHoverLR)
LRButton.bind('<Leave>', OnLeaveLR)
LRButton['font'] = myFont
LRButton.place(x=420, y= 620)

LRButton2 = Button(root,text="Linear Regression R o T",width=42,height=2,command=LRButton2Click, bg='green', relief='groove')
LRButton2.bind('<Enter>', OnHoverLR2)
LRButton2.bind('<Leave>', OnLeaveLR2)
LRButton2['font'] = myFont
LRButton2.place(x=820, y= 620)

TextButton = Button(root,text="Quantitative Stats",width=42,height=2,command=textbuttonClick, bg='green', relief='groove')
TextButton.bind('<Enter>', OnHoverText)
TextButton.bind('<Leave>', OnLeaveText)
TextButton['font'] = myFont
TextButton.place(x=620, y= 680)

root.state('zoomed')
root.mainloop()