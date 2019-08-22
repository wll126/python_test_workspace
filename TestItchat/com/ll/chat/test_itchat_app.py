# coding:utf-8

import itchat
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pandas import DataFrame

def count_sex_proportion():
    # 统计性别比例
    itchat.auto_login(hotReload=True)
    # 获取好友列表信息
    friends=itchat.get_friends()
    # friends=itchat.get_friends(update=True)[0:]
    print(friends)
    male=female=other=0
    for i in friends[1:]:
        # 遍历好友列表
        sex=i['Sex']
        if sex==1:
            male+=1
        elif sex==2:
            female+=1
        else:
            other+=1
    # 计算朋友总数
    total=len(friends[1:])
    # 打印结果
    print('male:%.2f%%' % (float(male)/total*100))
    print('female:%.2f%%' % (float(female)/total*100))
    print('other:%.2f%%' % (float(other)/total*100))
    # 画个图来看看
    draw_result(male,female,other)
    get_province(itchat.get_friends())

def get_province(friends):
    # 将好友所在省份信息保存到excel文件中
    nickName=sex=province=city=signature=[]
    nameList={'NickName':nickName,'Sex':sex,'Province':province,'City':city,'Signature':signature}
    for friend in friends:
        for k,v in nameList:
            v.append(friend[k])
    [ v.append(friend[k]) for friend in friends for k,v in nameList]
    frame=DataFrame(nameList)
    frame.to_csv('data.csv', index=True)

def draw_result(male,female,other):
    # 用图来展示结果
    lables=['man','female','unknow']
    X=[male,female,other]
    fig=plt.figure()
    plt.pie(X,labels=lables,autopct='%1.2f%%')
    plt.title('Pie chart')
    plt.show()
    plt.savefig('Piechart.jpg')


draw_result(20.20,70.70,10.10)
