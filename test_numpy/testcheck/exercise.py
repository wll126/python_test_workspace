#!/usr/bin/python
# -*- coding : utf-8 -*-
'''
 project = 'test_numpy'
 file_name='exerside'
 author ： wll
 now：2019/9/3 14:30
 version 1.0
'''
import numpy as np
from scipy import stats

data=np.array([[43,9],[44,4]])
# 卡方值，p值，自由度，期望值
v,p,dof,expected =stats.chi2_contingency(data)
print("卡方值x^2={v},p值p={p},自由度df={dof},期望u={expected}".format(v=v,p=p,dof=dof,expected=expected))
