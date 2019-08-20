# coding:utf-8

import itchat
import numpy
import matplotlib


def count_sex_proportion():
    # 统计性别比例
    itchat.login()
    # 获取好友列表信息
    friends=itchat.get_friends(update=True)[0:]
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
