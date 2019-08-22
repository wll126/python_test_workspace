# coding:utf8
import itchat
from itchat.content import *

"""微信消息处理"""
"""
收到的消息= {
'MsgId': '3390426259707504553', 
'FromUserName': '@917d7afb1612f591fd92470d3b5e475dbb90c713fe3ce242f6fbdc8c63fd3afc', 
'ToUserName': 'filehelper', 
'MsgType': 1, 
'Content': '[撇嘴]', 
'Status': 3, 
'ImgStatus': 1, 
'CreateTime': 1566269303, 
'VoiceLength': 0, 
'PlayLength': 0, 
'FileName': '', 
'FileSize': '', 
'MediaId': '', 
'Url': '', 
'AppMsgType': 0, 
'StatusNotifyCode': 0, 
'StatusNotifyUserName': '', 
'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 
'ForwardFlag': 0,
 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 3390426259707504553, 'OriContent': '', 'EncryFileName': '', 'User': <User: {'UserName': 'filehelper', 'MemberList': <ContactList: []>}>, 'Type': 'Text', 'Text': '[撇嘴]'}

"""


# 注册消息响应事件，消息类型为itchat.content.TEXT 文本消息
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    print("收到的消息=",msg)
    itchat.send('%s:%s' %(msg['Type'],msg['Text']), msg['FromUserName'])
    # return msg['Text']
    # @c554e645826b58d2a673b49f7305fa4d


@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    # 下载文件
    # msg['Text'] 是一个文件下载函数，传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    # 将下载好的文件发送给发送者
    return '@%s@%s' % ({'Picture':'img','Video':'vid'}.get(msg['Type'],'file'),msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    # 添加好友
    itchat.add_friend(**msg['Text'])
    # 加完好友后给好友打个招呼
    itchat.send_msg('Nice to see you !', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # 处理群聊消息
    if msg['isAt']:
        itchat.send_msg("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'],msg['Text']), toUserName=msg['FromUserName'])
        itchat.send(u'@%s\u2005I received : %s' % (msg['ActualNickName'],msg['Content']),msg['FromUserName'])
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)


def get_normal_friends():
    itchat.auto_login(hotReload=True)  # 登录微信,hotReload保持登录
    friends=itchat.get_friends()
    print(friends)
    #  获取好友信息
    me=itchat.search_friends()
    print(me)
    # 查询某个好友
    she=itchat.search_friends(userName='@c554e645826b58d2a673b49f7305fa4d')
    print(she)
    he=itchat.search_friends(name='刘先生')
    print(he)
    her=itchat.search_friends(wechatAccount='古早')
    print(her)

def get_public_number():
    # 获取公众号信息
    all=itchat.get_mps()
    print(all)
    # 搜索公众号
    some=itchat.search_mps(userName='@abcdefg1234567')
    print(some)
    other=itchat.search_mps(name='LitterCoder')

def get_group_chat():
    # 获取群聊信息
    all=itchat.get_chatrooms()
    for a in all: print(a)
    # 获取特定群聊
    s=itchat.search_chatrooms(name='LitterCoder')
    print(s)
    # 获取群聊用户列表
    memberlist=itchat.update_chatroom('@abcdefg1234567')
    print(memberlist)

def change_group():
    meblist=itchat.get_friends()[1:]
    # 创建群聊
    chatroom=itchat.create_chatroom(meblist,'群聊名称')
    # 删除群聊内的用户
    itchat.delete_member_from_chatroom(chatroom,meblist[0])
    # 增加用户
    itchat.add_member_into_chatroom(chatroom,meblist[0])


itchat.auto_login(hotReload=True)     # 登录微信,hotReload保持登录
# 给文件助手发消息
# itchat.send_msg('Hello ,filehelper', toUserName='filehelper')
get_normal_friends()
itchat.run()





