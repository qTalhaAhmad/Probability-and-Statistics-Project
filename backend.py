import csv
import math
from os import sep
import statistics
import scipy.stats
import numpy as np
import pandas as pd
from matplotlib import colors
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#                      --Temprature-Rainfall 1901-2016--
#    19F-0113 (CS),    19F-0171 (CS),      19F-0254 (CS),       19F-0931 (SE)
#    Talha Ahmad,      M. Talha Shehroze,     Muhammad Farhan,     Daniyal Ahmed

# Reading Data from CSV.
dataset1 = pd.read_csv(r'dataset\19012016.csv')

# Taking Mean of Monthly Temprature and Rainfall from 1901-2016
def meanTempRainFunc():
    tempMean=dataset1['Temperature (Celsius)'].mean().round(3)
    strTempMean=str(tempMean)
    temp="->Average Monthly Temprature (Celsius) from 1901-2016 was: "
    file.write(temp)    
    file.write(strTempMean)
    file.write(" °C\n")
    
    rainMean=dataset1['Rainfall (MM)'].mean().round(3)
    strrainMean=str(rainMean)
    temp0="->Average Monthly Rainfall (MM) from 1901-2016 was: "
    file.write(temp0)    
    file.write(strrainMean)
    file.write(" mm\n\n")
        
# Taking Median of Monthly Temprature and Rainfall from 1901-2016
def medianTempRainFunc():
    tempMedian=dataset1['Temperature (Celsius)'].median()
    strTempMedian=str(tempMedian)
    temp="->Median Monthly Temprature (Celsius) from 1901-2016 was: "
    file.write(temp)    
    file.write(strTempMedian)
    file.write(" °C\n")

    rainMedian=dataset1['Rainfall (MM)'].median()
    strRainMedian=str(rainMedian)
    temp0="->Median Monthly Rainfall (MM) from 1901-2016 was: "
    file.write(temp0)
    file.write(strRainMedian)
    file.write(" mm\n\n")

# Descriptive Statistics of Dataset of Temprature and Rainfall from 1901-2016
def dataDescript():
    describeData1=dataset1[['Temperature (Celsius)']].describe().round()
    print(describeData1)
    describeData2=dataset1[['Rainfall (MM)']].describe().round()
    print(describeData2)

# Taking Minimum and Maximum of Monthly Temprature from 1901-2016
tempMin=dataset1['Temperature (Celsius)'].min()
tempMax=dataset1['Temperature (Celsius)'].max()

# Taking Minimum and Maximum Value of Monthly Rainfall from 1901-2016
rainMin=dataset1['Rainfall (MM)'].min()
rainMax=dataset1['Rainfall (MM)'].max()

# Taking Minimum and Maximum Row of Monthly Temprature from 1901-2016
def minMaxTempratureRow():    
    tempMinRow = dataset1.loc[dataset1['Temperature (Celsius)'] == tempMin]
    temp="->Minimum Monthly Temprature (Celsius) from 1901-2016 was in:"
    file.write(temp+'\n')
    temp1=tempMinRow.to_string(index=False)
    file.write(temp1+'\n\n')
    tempMaxRow = dataset1.loc[dataset1['Temperature (Celsius)'] == tempMax]
    temp0="->Maximum Monthly Temprature (Celsius) from 1901-2016 was in:"    
    file.write(temp0+'\n')
    temp2=tempMaxRow.to_string(index=False)    
    file.write(temp2+'\n\n')

# Taking Minimum and Maximum Row of Monthly Rainfall from 1901-2016
def minMaxRainfallRow():
    rainMinRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMin]    
    temp="->Minimum Monthly Rainfall (MM) from 1901-2016 was in:"
    file.write(temp+'\n')
    temp1=rainMinRow.to_string(index=False)
    file.write(temp1+'\n\n')
    rainMaxRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMax]
    temp0 ="->Maximum Monthly Rainfall (MM) from 1901-2016 was in:"
    file.write(temp0+'\n')
    temp2=rainMaxRow.to_string(index=False)
    file.write(temp2+'\n\n')

# Reading Data from CSV by Month.
janDataset = dataset1.loc[dataset1['Month'] == 'January']
febDataset = dataset1.loc[dataset1['Month'] == 'February']
marDataset = dataset1.loc[dataset1['Month'] == 'March']
aprDataset = dataset1.loc[dataset1['Month'] == 'April']
mayDataset = dataset1.loc[dataset1['Month'] == 'May']
junDataset = dataset1.loc[dataset1['Month'] == 'June']
julDataset = dataset1.loc[dataset1['Month'] == 'July']
augDataset = dataset1.loc[dataset1['Month'] == 'August']
sepDataset = dataset1.loc[dataset1['Month'] == 'September']
octDataset = dataset1.loc[dataset1['Month'] == 'October']
novDataset = dataset1.loc[dataset1['Month'] == 'November']
decDataset = dataset1.loc[dataset1['Month'] == 'December']

# Calculating Mean Temprature and Rain by Month.
janTempMean=janDataset['Temperature (Celsius)'].mean();    janRainMean=janDataset['Rainfall (MM)'].mean()
febTempMean=febDataset['Temperature (Celsius)'].mean();    febRainMean=febDataset['Rainfall (MM)'].mean()
marTempMean=marDataset['Temperature (Celsius)'].mean();    marRainMean=marDataset['Rainfall (MM)'].mean()
aprTempMean=aprDataset['Temperature (Celsius)'].mean();    aprRainMean=aprDataset['Rainfall (MM)'].mean()
mayTempMean=mayDataset['Temperature (Celsius)'].mean();    mayRainMean=mayDataset['Rainfall (MM)'].mean()
junTempMean=junDataset['Temperature (Celsius)'].mean();    junRainMean=junDataset['Rainfall (MM)'].mean()
julTempMean=julDataset['Temperature (Celsius)'].mean();    julRainMean=julDataset['Rainfall (MM)'].mean()
augTempMean=augDataset['Temperature (Celsius)'].mean();    augRainMean=augDataset['Rainfall (MM)'].mean()
sepTempMean=sepDataset['Temperature (Celsius)'].mean();    sepRainMean=sepDataset['Rainfall (MM)'].mean()
octTempMean=octDataset['Temperature (Celsius)'].mean();    octRainMean=octDataset['Rainfall (MM)'].mean()
novTempMean=novDataset['Temperature (Celsius)'].mean();    novRainMean=novDataset['Rainfall (MM)'].mean()
decTempMean=decDataset['Temperature (Celsius)'].mean();    decRainMean=decDataset['Rainfall (MM)'].mean()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthsN = [1,2,3,4,5,6,7,8,9,10,11,12]
avgTemp = [janTempMean,febTempMean,marTempMean,aprTempMean,mayTempMean,junTempMean,julTempMean,augTempMean,sepTempMean,octTempMean,novTempMean,decTempMean]
avgRain = [janRainMean,febRainMean,marRainMean,aprRainMean,mayRainMean,junRainMean,julRainMean,augRainMean,sepRainMean,octRainMean,novRainMean,decRainMean]

avgTRdata = [avgTemp,avgRain]

months2 = [ 'November','December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
avgRain2 = [novRainMean,decRainMean,janRainMean,febRainMean,marRainMean,aprRainMean,mayRainMean,junRainMean,julRainMean,augRainMean,sepRainMean,octRainMean]

# Bar Graph of Pakistan's Average Temprature/Month from 1901-2016
def avgTMBarG():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])    
    ax.bar(months,avgTemp,color='red')
    plt.xlabel("x - Month")
    plt.ylabel("y - Temprature (°C)")
    plt.title("Pakistan's Average Temprature/Month from 1901-2016")
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

# Bar Graph of Pakistan's Average Rainfall/Month from 1901-2016
def avgRMBarG():
    fig1 = plt.figure()
    ax = fig1.add_axes([0.1,0.1,0.8,0.8])
    ax.bar(months2,avgRain2,color='green')
    plt.xlabel("x - Month")
    plt.ylabel("y - Rainfall (mm)")
    plt.title("Pakistan's Average Rainfall/Month from 1901-2016")
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

def tempRainMultiBarChart():
    fig2 = plt.figure()
    ax = fig2.add_axes([0.1,0.1,0.8,0.8])
    X_axis = np.arange(len(months))
    plt.bar(X_axis - 0.2, avgTemp, 0.4, label = 'Temp (°C)', color='red')
    plt.bar(X_axis + 0.2, avgRain, 0.4, label = 'Rain (mm)', color='green')
    plt.xticks(X_axis, months)
    plt.xlabel("Months")
    plt.ylabel("Temp (°C), Rain (mm)")
    plt.title("Pakistan's Temprature/Month in each Month")
    plt.legend()
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

# Scatter Plot of Pakistan's Average Temprature/Month from 1901-2016 (Showing Relation)
def scatterTempGraphFunc():
    fig3 = plt.figure()    
    a1 = fig3.add_axes([0.1,0.1,0.8,0.8])
    a1.plot(monthsN, avgTemp, 'r-')
    a1.set_xlabel('Months')    
    a1.set_ylabel('Temp (°C)')
    
    #fig3.legend(labels = ('Temp (°C)'),loc='upper center')
    plt.title("Pakistan's Temprature in each Month")
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

# Scatter Plot of Pakistan's Average Temprature/Month from 1901-2016 (Showing Relation)
def scatterRainGraphFunc():
    fig5 = plt.figure()    
    a1 = fig5.add_axes([0.1,0.1,0.8,0.8])
    
    a1.plot(monthsN, avgRain, 'g-')
    a1.set_xlabel('Months')    
    a1.set_ylabel('Rain (mm)')
    
    #fig5.legend(labels = ('Rain (mm)'),loc='upper center')
    plt.title("Pakistan's Rainfall in each Month")
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

# Scatter Plot of Pakistan's Average Rainfall-Temprature/Month from 1901-2016 (Showing Relation)
def scatterMultiGraphFunc():
    fig6 = plt.figure()    
    a1 = fig6.add_axes([0.1,0.1,0.8,0.8])
    a1.plot(monthsN, avgTemp, 'ro-')
    a1.set_xlabel('Months')    
    a1.set_ylabel('Temp (°C)')
    
    a2 = a1.twinx()
    a2.plot(monthsN, avgRain, 'go-')
    a2.set_ylabel('Rain (mm)')

    fig6.legend(labels = ('Temp (°C)','Rain (mm)'),loc='upper center')
    plt.title("Relationship b/w Pakistan's Rainfall/Temprature in each Month")
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

def boxPlotTempRain():
    fig4 = plt.figure()
    ax = fig4.add_axes([0.1,0.1,0.8,0.8])
    ax.set_xticklabels(['Temprature', 'Rain']) # warning for fixed labels.
    bp = ax.boxplot(avgTRdata)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

## distribution -- analysis

## covariance / correlation

## regression -- prediction


###              FunctionCalls()

file = open("dataset/statstext.txt","w") 
meanTempRainFunc()
medianTempRainFunc()
#    dataDescript()
minMaxTempratureRow()
minMaxRainfallRow()
file.close()
#    avgTMBarG()
#    avgRMBarG()
#    tempRainMultiBarChart()
#    boxPlotTempRain()
#    scatterTempGraphFunc()
#    scatterRainGraphFunc()
#    scatterMultiGraphFunc()
#    boxPlotTempRain()

#_____________________________________________________________________________________________________________
#   Data can be editable. At any stage, we can add or delete any values in the data set.

#   Statistical analysis should be consisted of, Graphical and tabular data 
#   representation, Descriptive Statistical analysis, Probability distributions. 
#   Finally, modeling and Predictions using Regression Models.

#   Your designed application should be intelligent in doing statistical analysis. 

#   The work will be evaluated on following
#       a. How many appropriate statistical tools have been used?
#       b. How attractive and intelligent your application is?




#   Paste all codes on a word file in fount size 9 and line space 1. Paste screenshots of your application
#   with different features/results on a word file. 
#   Finally, your results and recommendation about the data should be detailed pasted on that word file.





# Probability Distribution 

# --Discrete
# 
# ----Binomial
# ----Poisson
# ----Hypergeometric
# 
# --Continuous
# 
# ----Uniform
# ----Normal
# 
# Covariance
# Correlation
# 
# Deterministic
# Probabilistic

# Error term
