# coding=utf-8
import string

from suds.client import Client


# soap 客户端
# 使用suds 客户端调用webservice方法
url="http://10.106.72.6:8000/?wsdl"
client=Client(url=url)
print(client)

# 调用第一个接口
res=client.service.say_hello1('zhansan',1)
print(res)
print('='*20)

res=client.service.say_hello2('lisi',2)
print(res)
print('='*20)

res=client.service.say_hello3('wanwu',3)
print(res)
print('='*20)

res=client.service.say_hello4('liuliu',4)
print(res)
print('='*20)




