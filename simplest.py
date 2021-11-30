import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
 
# Dataset
x = np.array([0,45.11,54,62.89,67.33,85.78])  #设置x轴数据，以','分隔
y = np.array([0,0.06,0.09,0.12,0.14,0.23])  #设置y轴数据，需与x轴数据一一对应
 
X_Y_Spline = make_interp_spline(x, y)
 
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
 
# Plotting the Graph
plt.scatter(x,y,s=20)
plt.plot(X_, Y_)
plt.title("图表标题",fontproperties="SimHei",fontsize=16)  #设置图表标题
plt.xlabel("x轴标签",fontproperties="SimHei",fontsize=12,loc="right")  #设置x轴标签
plt.ylabel("y轴标签",fontproperties="SimHei",fontsize=12,loc="top",rotation=0,labelpad=-30) #设置y轴标签
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
#plt.axis([0,89,0,0.28])
plt.savefig('图表名称.png',dpi=900,bbox_inches='tight')  #设置图表名称
plt.show()