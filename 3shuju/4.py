import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import math

def autolabel (ax):
    for rect in ax.patches:
        y = rect.get_y() + rect.get_height()/2

        width = rect.get_width()
        width = width if math.isnan(width) == False else 0
        ax.text(x=width,y=y,s=f"{int(width)}")

values ={
    "A":[100,90,70,100,50,90],
    "B":[85,20,60,30,90,100]
}

df = pd.DataFrame(values)
print(df)
ax = df.plot(kind="barh")
autolabel(ax)

plt.show()