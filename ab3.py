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

#
print("\n\n") # this is the start of main code. 
#

# Reading Data from CSV.
dataset1 = pd.read_csv (r'dataset\Rainfall_19012016.csv')
dataset2 = pd.read_csv (r'dataset\Temperature_19012016.csv')
dataset3 = pd.read_csv (r'dataset\19012016.csv', usecols = ['Temperature (Celsius)','Rainfall (MM)'])
dataset4 = pd.read_csv(r'dataset\19012016.csv')

# Merging both datasets into 1 with same Month and Year
dataset5 = pd.merge(dataset1, dataset2, on=["Month","Year"])
dataset5 = dataset5[["Month", "Year",'Rainfall (MM)','Temperature (Celsius)']]

#print (dataset5); print("\n")

# Taking Mean of Monthly Temprature and Rainfall from 1901-2016
def meanTempRainFunc():
    tempMean=dataset5['Temperature (Celsius)'].mean()
    print ("Average Monthly Temprature (Celsius) from 1901-2016 is:",tempMean, "Celsius")
    rainMean=dataset5['Rainfall (MM)'].mean()
    print ("Average Monthly Rainfall (MM) from 1901-2016 is:",rainMean, "MM")

# Taking Median of Monthly Temprature and Rainfall from 1901-2016
def medianTempRainFunc():
    tempMedian=dataset5['Temperature (Celsius)'].median()
    print ("Median Monthly Temprature (Celsius) from 1901-2016 is:",tempMedian, "Celsius")
    rainMedian=dataset5['Rainfall (MM)'].median()
    print ("Median Monthly Rainfall (MM) from 1901-2016 is:",rainMedian, "MM")

# Descriptive Statistics of Dataset of Temprature and Rainfall from 1901-2016
def dataDescript():
    describeData=dataset5[['Temperature (Celsius)','Rainfall (MM)']].describe().round()
    print(describeData)

# Taking Minimum and Maximum of Monthly Temprature from 1901-2016
tempMin=dataset5['Temperature (Celsius)'].min()
tempMax=dataset5['Temperature (Celsius)'].max()

# Taking Minimum and Maximum Value of Monthly Rainfall from 1901-2016
rainMin=dataset5['Rainfall (MM)'].min()
rainMax=dataset5['Rainfall (MM)'].max()

# Taking Minimum and Maximum Row of Monthly Temprature from 1901-2016
def minMaxTempratureRow():
    tempMinRow = dataset2.loc[dataset2['Temperature (Celsius)'] == tempMin]
    print ("Minimum Monthly Temprature (Celsius) from 1901-2016 is:")
    print(tempMinRow)
    print("\n")
    tempMaxRow = dataset2.loc[dataset2['Temperature (Celsius)'] == tempMax]
    print ("Maximum Monthly Temprature (Celsius) from 1901-2016 is:")
    print(tempMaxRow)


# Taking Minimum and Maximum Row of Monthly Rainfall from 1901-2016
def minMaxRainfallRow():
    rainMinRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMin]
    print ("Minimum Monthly Rainfall (MM) from 1901-2016 is:")
    print(rainMinRow)
    print("\n")
    rainMaxRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMax]
    print ("Maximum Monthly Rainfall (MM) from 1901-2016 is:")
    print(rainMaxRow)

# Reading Data from CSV by Month.
janDataset = dataset4.loc[dataset4['Month'] == 'January']
febDataset = dataset4.loc[dataset4['Month'] == 'February']
marDataset = dataset4.loc[dataset4['Month'] == 'March']
aprDataset = dataset4.loc[dataset4['Month'] == 'April']
mayDataset = dataset4.loc[dataset4['Month'] == 'May']
junDataset = dataset4.loc[dataset4['Month'] == 'June']
julDataset = dataset4.loc[dataset4['Month'] == 'July']
augDataset = dataset4.loc[dataset4['Month'] == 'August']
sepDataset = dataset4.loc[dataset4['Month'] == 'September']
octDataset = dataset4.loc[dataset4['Month'] == 'October']
novDataset = dataset4.loc[dataset4['Month'] == 'November']
decDataset = dataset4.loc[dataset4['Month'] == 'December']

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

# Bar Graph of Pakistan's Average Temprature/Month from 1901-2016
def avgTMG():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])    
    ax.bar(months,avgTemp,color='red')
    plt.xlabel("x - Month")
    plt.ylabel("y - Temprature (°C)")
    plt.title("Pakistan's Average Temprature/Month from 1901-2016")
    plt.show()

# Bar Graph of Pakistan's Average Rainfall/Month from 1901-2016
def avgRMG():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    ax.bar(months,avgRain,color='green')
    plt.xlabel("x - Month")
    plt.ylabel("y - Rainfall (mm)")
    plt.title("Pakistan's Average Rainfall/Month from 1901-2016")
    plt.show()

# Rainfall on X, Temprature on Y, Bar Graph, Shows a trend.
def barGraphFunc():
    dataset3.plot.bar(x = 'Rainfall (MM)', y = 'Temperature (Celsius)')
    plt.show()

# Scatter Plot of Pakistan's Average Rainfall/Month from 1901-2016 (Showing Relation)
def scatterGraphFunc():        
    fig = plt.figure()    
    
    a1 = fig.add_axes([0.1,0.1,0.8,0.8])    
    a1.plot(monthsN, avgTemp, 'ro-')
    a1.set_xlabel('Months')    
    a1.set_ylabel('Temp (°C)')
    
    a2 = a1.twinx()
    a2.plot(monthsN, avgRain, 'go-')
    a2.set_ylabel('Rain (mm)')

    fig.legend(labels = ('Temp (°C)','Rain (mm)'),loc='upper center')
    plt.show()

#distribution -- analysis
#regression -- prediction


### Function Calling

# meanTempRainFunc()
# medianTempRainFunc()
# dataDescript()
# minMaxTempratureRow()
# minMaxRainfallRow()

### avgTMG()
### avgRMG()

# barGraphFunc()
scatterGraphFunc()

#
print("\n") # this is the end of  main code. 
#