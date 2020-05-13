import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import math

# 散点
# n = 1024
# x = np.random.normal(0,1,n)
# y = np.random.normal(0,1,n)
# t = np.arctan2(y,x)

# #plt.scatter(x,y,s=75,c=t,alpha =0.5)

# plt.scatter(np.arange(5),np.arange(5))
# # plt.xlim((-1.5,1.5))
# # plt.ylim((-1.5,1.5))
# plt.xticks(())
# plt.yticks(())
# plt.show



def autolabl(ax):
    for rect in ax.patches:
        x = rect.get_x()+rect.get_width()/3

        height = rect.get_height()
        height = height if math.isnan(height)  == False else 0
        ax.text(x = x,y=height,s=f'{int(height)}')

dates =[d.strftime("%y-%m-%d") for d in pd.date_range("20200513",periods=6)]
values = [100,80,90,70,50,85]

df = pd.DataFrame(values,index=dates,columns=list("A"))
print(df)
ax = df.plot(kind='bar',stacked=True)
autolabl(ax)

plt.show()
