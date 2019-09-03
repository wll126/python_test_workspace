#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 project = 'test_numpy'
 file_name='exercises'
 author ： wll
 now：2019/9/2 15:41
 version 1.0
'''
import os

"""
练习： 2-2
生成一个pandas数据框，其x列为0~10秒的时间戳，频率为10hz,y列数据的值为1.5Hz的正弦值，z列为对应的余弦值。
将x列命名为"时间",y列命名为"Yvals",z命名为"ZVals"
展示该数据框的开始行。
取出 "Yvals" 和 "Zvals"中第10~15行的数据，并将其写入"out.txt"文件
输出存放路径
"""
from matplotlib import pyplot
import numpy as np
import pandas as pd
from matplotlib.pyplot import plot, xlabel, ylabel, savefig
# 生成0-10的时间戳，频率为10hz，对应周期为0.1s
x=np.arange(0,10,0.1)
# 生成频率为1.5Hz的正弦值 公式2pi*频率
y=np.sin(x) # * 2 * np.pi*1.5)
# 生成余弦值
z=np.cos(x)
# 生成数据框
df=pd.DataFrame({'时间':x,'Yvals':y,'ZVals':z})
# 看下图形

# 该数据框的开始行
print(df.head())
# 取出 "Yvals" 和 "Zvals"中第10~15行的数据，并将其写入"out.txt"文件
data=df[['Yvals','ZVals']][9:15]
print(type(data))
data=df.iloc[9:15,[1,2]]
print(type(data))
with open('out.txt','w+') as f:
    f.write('Yvals,ZVals\n')
    for d in data.values:
        f.write(','.join(str(i) for i in d)+'\n')
# 存放路径
path=os.path.dirname(os.path.realpath(__file__))
print("当前路径为：",path)
# 看图
plot(x,y,z)
pyplot.show()




