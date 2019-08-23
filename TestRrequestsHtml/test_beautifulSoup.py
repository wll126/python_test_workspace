# coding:utf-8

from bs4 import BeautifulSoup
from lxml import etree

htmlhandle=None
with open('test2.html','r',encoding='utf-8') as f:
    htmlhandle=f.read()

soup=BeautifulSoup(htmlhandle,'lxml')
# 获取p标签内容text
print(soup.p.string)
# 提取名称
print('name:',soup.p.name)
# 获取属性 attrs
print('attrs:',soup.nav.attrs)
# 获取属性 attrs
print('attrs[class]:',soup.nav.attrs['class'])

# 获取直接子节点  contents,返回列表类型  children
print('contents:',soup.div.contents)
print('children:',soup.div.children)
# 获取所有子孙节点
print('all children:',soup.div.descendants)

