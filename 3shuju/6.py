import pandas as pd 
import numpy as np 
import matplotlib.dates as mdates 
import matplotlib.pyplot as plt 
import math

def autolable(ax):
    for rect in ax.patches:
        x = rect.get_x() + rect.get_width()/2

        height = rect.get_height()
        height = height if math.isnan(height) == False else 0
        ax.text(x=x,y=height,s=f"{int(height)}")

dates = [d.strftime("%y-%m-%d") for d in pd.date_range("20200514",periods=6)]

values ={
    "A":[100,90,70,100,50,90],
    "B":[85,20,60,30,90,100]
}

df = pd.DataFrame(values,index=dates)
df = df.sort_index(axis=0,ascending=False)
ax = df.plot(kind = "bar")
autolable(ax)

plt.show()