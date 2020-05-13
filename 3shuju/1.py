import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x = np.linspace(-3,3,50)
# y1 = 2*x+1
# y2 = x**2

# plt.figure()
# plt.plot(x,y1)

# # plt.figure(num=3,figsize=(8,5))
# # plt.plot(x,y2)
# # plt.plot(x,y1,color='red',linewidth = 1.0,linestyle = '--')


##设置坐标轴名称
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# plt.xlabel("I am x")
# plt.ylabel("I am y")

##自定义坐标轴单位名称
# new_ticks = np.linspace(-1,2,3)
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([-2,-1.8,-1,1.22,3,],
#     [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

##设置坐标轴位置
# # gca = 'get current axis
# ax = plt.gca()
# ax.spines['right'].set_color('none')  #隐藏右边框
# ax.spines['top'].set_color('none')    #隐藏上边框
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',0)) # bottom在y轴0
# ax.spines['left'].set_position(('data',1))   # left在x轴1

##添加图例
# plt.figure(num=3,figsize=(8,5))
# l1,=plt.plot(x,y2,label = 'up')
# l2,=plt.plot(x,y1,color='red',linewidth = 1.0,linestyle = '--',label = 'down')
# plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')  #upper right


##添加标注
x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position(('left'))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)

plt.show()

# s = pd.Series([1,3,5,7,6,9])
# print(s)
# s.plot(grid=True)
# plt.show()