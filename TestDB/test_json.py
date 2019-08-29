# coding:utf-8

import json
"""
loads 将json字符串转化成JSON对象   要求用双引号
dumps 将JSON对象转成字符串 intent指定字符缩进个数 ensure_ascii=False 输出中文
"""

str='''
[{"name":"Bob","gender":"male","birthday":"1992-10-10"},
 {"name":"张1","gender":"fema","birthday":"1995-10-10"},
 {"name":"Sel","gender":"fema","birthday":"1995-10-10"}]
'''
print(type(str))
data=json.loads(str)
print(data)
print(type(data))
strdata=json.dumps(data,indent=2,ensure_ascii=False)
print(type(strdata),strdata)