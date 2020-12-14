import numpy as np
import pandas as pd
import csv
import os
import matplotlib.pyplot as py
import statistics
def plotfun(Speed,Powercurve,start,end):
    WindSpeed=[]
    for i in range(start,end+1):
        WindSpeed.append(Speed[i])

    curve=[]
    for i in range(start,end+1):
        curve.append(Powercurve[i])
    py.plot(WindSpeed,curve)

def findmean(arr,start,end):
    l=[]
    for i in range(start,end):
        l.append(arr[i])
    x = statistics.mean(l)
    print("the energy output of the windmill is ",x)
        

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
data=pd.read_csv(r"C:\Users\aruns\Desktop\WINDTURBINE\data.csv.zip")#@(the location of the data file must be pasted inside the coluns.)
new_data=({
    "Time":data['Date/Time'],
    "Power":data['LV ActivePower (kW)'],
    "Speed":data['Wind Speed (m/s)'],
    "Power_curve":data['Theoretical_Power_Curve (KWh)'],
    "Direction":data['Wind Direction (°)']  
})

q=int(input("Do you need to calculate the output energy of windmill in hours or in minutes or in days?(1=hours/0=minutes/2=days): "))
if q==1:
    a=int(input("Number of hours prediction you need: "))
    b=6#i have a constant value this is the number of columns because the mini value i took is 1hour=6columns
    c=a*b
elif q==0:
    a=int(input("Number of minutes prediction you need: "))
    b=10#though the given data has prediction for 10minutes so i took 10min=1column
    c=a//b
    #the bellow code will calculate in days
elif q==2:
    a=int(input("Number of days prediction you need: "))
    b=144
    c=a*b

plotfun(new_data["Speed"],new_data["Power_curve"],0,c)
findmean(new_data["Power_curve"],0,c)
