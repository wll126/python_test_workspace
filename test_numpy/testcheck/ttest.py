#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 project = 'test_numpy'
 file_name='ttest'
 author ： wll
 now：2019/9/3 11:19
 version 1.0
 t 检验
'''

import numpy as np
from scipy import stats

# 生成数据
# np.random.seed(123)
race1=np.round(np.random.randn(20)*10+90)
race2=np.round(np.random.randn(20)*10+85)

# t检验
(t,pVal)=stats.ttest_rel(race1,race2)
# 显示结果
print("检验结果: 两者差异水平等于{0:5.3f} ".format(pVal))
