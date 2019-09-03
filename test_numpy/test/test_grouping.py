#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 project = 'test_numpy'
 file_name='test_grouping'
 author ： wll
 now：2019/9/2 14:51
 version 1.0
 测试数据分组
'''
import pandas as pd
import matplotlib.pyplot as plt

d={
    'gender':['f','f','m','f','m','m','f','m','f','m','m'],
    'TV':[3.4,3.5,2.6,4.7,4.1,4.1,5.1,3.9,3.7,2.1,4.3]
}
data=pd.DataFrame(d)
# -----------------------------------------------------
# 给数据分组
grouped=data.groupby('gender')
# 进行一些汇总统计
print(grouped.describe())
# 绘制数据
grouped.boxplot()
plt.show()

#--------------------------------------------------------
# 以数据框的形式获取数组
df_female=grouped.get_group('f')
# 得到对应的numpy数组
values_female=grouped.get_group('f').values




