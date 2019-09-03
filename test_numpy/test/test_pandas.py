#!/usr/bin/python
# -*-coding:utf-8-*-

import numpy as np
import pandas as pd

t=np.arange(0,10,0.1)
x=np.sin(t)
y=np.cos(t)
# 定义列数据  列名：数据list
df=pd.DataFrame({'Time':t,'x':x,'y':y})
# 获取列数据
data=df[['Time','y']]
# 获取首5行
print(data.head())
# 获取尾5行
print(data.tail())
#  获取第5行到第10行
print(data[4:10])
# df
print(df[['Time','y']][4:10])
#   使用标准的行/列  5-10行,  0 和 2 列
print(df.iloc[4:10,[0,2]])
# 直接访问数据 返回一个numpy 数组
print(data.values)
