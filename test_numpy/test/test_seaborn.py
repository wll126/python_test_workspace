#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 project = 'test_numpy'
 file_name='test_seaborn'
 author ： wll
 now：2019/9/2 15:27
 version 1.0
  seabborn 生成美观的可视化图形
'''

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,7,50)
y=3+2*x+1.5*np.random.randn(len(x))
df=pd.DataFrame({'xData':x,'yData':y})
sns.regplot('xData','yData',data=df)
plt.show()

