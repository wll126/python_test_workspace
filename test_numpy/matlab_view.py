#!/usr/bin/python
# coding:utf-8
import os

'''
 一个python 脚本的简短演示
 作者： wll
 日期：2019年9月2日
 版本 1.0
'''
# 导入标准包
from matplotlib import pyplot
from matplotlib.pyplot import plot, xlabel, ylabel, savefig
from numpy import r_, sin, pi

# 生成时间的值  0-10 区间， 步长0.1
t=r_[0:10:0.1]
# 设定频率
freq=0.5
# 计算正弦值
x=sin(2*pi*freq*t)

# 切换目录
os.chdir('thomas')
# 绘制数据图形
plot(t,x)
# 格式化图形
xlabel('Time [sec]')
ylabel('Values')
# 生成图形文件
savefig('Sinewave.png',dpi=200)
# 展现图形
pyplot.show()
