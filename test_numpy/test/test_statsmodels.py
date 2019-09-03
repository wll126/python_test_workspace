#!/usr/bin/python
# -*- coding : utf-8 -*-
"""
 project = 'test_numpy'
 file_name='test_statsmodels'
 author ： wll
 now：2019/9/2 15:07
 version 1.0
 statsmodels 统计建模
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
import seaborn

x=np.arange(100)
y=0.5*x-20+np.random.randn(len(x))
df=pd.DataFrame({'x':x,'y':y})

# 使用patsy 包附加的公式语言拟合线性模型
model=sm.ols('y~x',data=df).fit()
print(model.summary())
