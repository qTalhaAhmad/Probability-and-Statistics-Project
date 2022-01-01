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

#                        Temprature-Rainfall 1901-2016
#    19F-0113 (CS),    19F-0171 (CS),      19F-0254 (CS),       19F-0931 (SE)
#    Talha Ahmad,      Talha Shehroze,     Muhammad Farhan,     Daniyal Ahmed

# Reading Data from CSV.
dataset1 = pd.read_csv(r'dataset\19012016.csv')

# Taking Mean of Monthly Temprature and Rainfall from 1901-2016
def meanTempRainFunc():
    tempMean=dataset1['Temperature (Celsius)'].mean()
    print ("Average Monthly Temprature (Celsius) from 1901-2016 is:",tempMean, "Celsius")
    rainMean=dataset1['Rainfall (MM)'].mean()
    print ("Average Monthly Rainfall (MM) from 1901-2016 is:",rainMean, "MM")

# Taking Median of Monthly Temprature and Rainfall from 1901-2016
def medianTempRainFunc():
    tempMedian=dataset1['Temperature (Celsius)'].median()
    print ("Median Monthly Temprature (Celsius) from 1901-2016 is:",tempMedian, "Celsius")
    rainMedian=dataset1['Rainfall (MM)'].median()
    print ("Median Monthly Rainfall (MM) from 1901-2016 is:",rainMedian, "MM")

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
    print ("Minimum Monthly Temprature (Celsius) from 1901-2016 is:")
    print(tempMinRow.to_string(index=False))
    print("\n")
    tempMaxRow = dataset1.loc[dataset1['Temperature (Celsius)'] == tempMax]
    print ("Maximum Monthly Temprature (Celsius) from 1901-2016 is:")
    print(tempMaxRow.to_string(index=False))

# Taking Minimum and Maximum Row of Monthly Rainfall from 1901-2016
def minMaxRainfallRow():
    rainMinRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMin]
    print ("Minimum Monthly Rainfall (MM) from 1901-2016 is:")
    print(rainMinRow.to_string(index=False))
    print("\n")
    rainMaxRow = dataset1.loc[dataset1['Rainfall (MM)'] == rainMax]
    print ("Maximum Monthly Rainfall (MM) from 1901-2016 is:")
    print(rainMaxRow.to_string(index=False))

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

months2 = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
avgRain2 = [decRainMean,janRainMean,febRainMean,marRainMean,aprRainMean,mayRainMean,junRainMean,julRainMean,augRainMean,sepRainMean,octRainMean,novRainMean]

# Bar Graph of Pakistan's Average Temprature/Month from 1901-2016
def avgTMBarG():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])    
    ax.bar(months,avgTemp,color='red')
    plt.xlabel("x - Month")
    plt.ylabel("y - Temprature (°C)")
    plt.title("Pakistan's Average Temprature/Month from 1901-2016")
    plt.show()

# Bar Graph of Pakistan's Average Rainfall/Month from 1901-2016
def avgRMBarG():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    ax.bar(months2,avgRain2,color='green')
    plt.xlabel("x - Month")
    plt.ylabel("y - Rainfall (mm)")
    plt.title("Pakistan's Average Rainfall/Month from 1901-2016")
    plt.show()

def tempRainMultiBarChart():
    X_axis = np.arange(len(months))
    plt.bar(X_axis - 0.2, avgTemp, 0.4, label = 'Temp (°C)', color='red')
    plt.bar(X_axis + 0.2, avgRain, 0.4, label = 'Rain (mm)', color='green')
    plt.xticks(X_axis, months)
    plt.xlabel("Months")
    plt.ylabel("Temp (°C), Rain (mm)")
    plt.title("Months/Temprature in each Month")
    plt.legend()
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


####   Function Calling
#meanTempRainFunc();print("\n")
#medianTempRainFunc();print("\n")
#dataDescript();print("\n")
#minMaxTempratureRow();print("\n")
#minMaxRainfallRow();print("\n")
#avgTMBarG()
#avgRMBarG()

#tempRainMultiBarChart()

#scatterGraphFunc()

#
print("\n") # this is the end of  main code. 
#

#   Data can be editable. At any stage, we can add or delete any values in the data set.

#   Statistical analysis should be consisted of, Graphical and tabular data 
#   representation, Descriptive Statistical analysis, Probability distributions. 
#   Finally, modeling and Predictions using Regression Models.

#   Your designed application should be intelligent in doing statistical analysis. The work will be evaluated on following
#       a. How many appropriate statistical tools have been used?
#       b. How attractive and intelligent your application is?

#   Paste all codes on a word file in fount size 9 and line space 1. Paste screenshots of your application
#   with different features/results on a word file. 
#   Finally, your results and recommendation about the data should be detailed pasted on that word file.
