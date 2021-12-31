import csv
import math
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
dataset3 = pd.read_csv (r'dataset\19012016.csv')

# Merging both datasets into 1 with same Month and Year
dataset4 = pd.merge(dataset1, dataset2, on=["Month","Year"])
dataset4 = dataset4[["Month", "Year",'Temperature (Celsius)','Rainfall (MM)']]

print (dataset4); print("\n")

# Taking Mean of Monthly Temprature and Rainfall from 1901-2016
def meanTempRainFunc():
    tempMean=dataset4['Temperature (Celsius)'].mean()
    print ("Average Monthly Temprature (Celsius) from 1901-2016 is:",tempMean, "Celsius")
    rainMean=dataset4['Rainfall (MM)'].mean()
    print ("Average Monthly Rainfall (MM) from 1901-2016 is:",rainMean, "MM")

# Taking Median of Monthly Temprature and Rainfall from 1901-2016
def medianTempRainFunc():
    tempMedian=dataset4['Temperature (Celsius)'].median()
    print ("Median Monthly Temprature (Celsius) from 1901-2016 is:",tempMedian, "Celsius")
    rainMedian=dataset4['Rainfall (MM)'].median()
    print ("Median Monthly Rainfall (MM) from 1901-2016 is:",rainMedian, "MM")

#
#
#
#
# Descriptive Statistics of Dataset of Temprature and Rainfall from 1901-2016
describeData=dataset4[['Temperature (Celsius)','Rainfall (MM)']].describe().round()
print(describeData)
print("\n")

# Taking Minimum and Maximum of Monthly Temprature from 1901-2016
tempMin=dataset4['Temperature (Celsius)'].min()
tempMax=dataset4['Temperature (Celsius)'].max()

# Taking Minimum and Maximum Value of Monthly Rainfall from 1901-2016
rainMin=dataset4['Rainfall (MM)'].min()
rainMax=dataset4['Rainfall (MM)'].max()

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

# Rainfall on X, Temprature on Y, Bar Graph, Shows a trend.
def barGraphFunc():
    dataset3.plot.bar(x = 'Rainfall (MM)', y = 'Temperature (Celsius)')
    plt.show()

# Rainfall on X, Temprature on Y, Scatter Plot, Shows a trend.
def scatterGraphFunc():
    dataset3.plot.scatter(x = 'Rainfall (MM)', y = 'Temperature (Celsius)')
    plt.show()

#distribution -- analysis
#regression -- prediction

meanTempRainFunc()
medianTempRainFunc()
minMaxTempratureRow()
minMaxRainfallRow()
barGraphFunc()
scatterGraphFunc()

#
print("\n\n") # this is the end of  main code. 
#