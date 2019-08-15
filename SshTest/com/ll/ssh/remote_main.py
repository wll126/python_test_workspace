#!/usr/bin/python3
# -*- coding:utf-8 -*-
import socket
import time

import paramiko
import threading


# 远程连接
def ssh2(ip,username,passwd,cmd):
    try:
        # ssh客户端
        ssh=paramiko.SSHClient()
        # 自动连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 开始连接
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            # 执行命令，返回输入输出异常信息
            stdin,stdout,stderr=ssh.exec_command(m)
            # stdin.write("Y")  # 简单交互 ，输入Y
            out =stdout.readlines()
            # 屏幕输出
            for o in out:
                print("输出:",o)
        print('%s\tOK\n' % (ip))
        # 关闭ssh连接
        ssh.close()
    except:
        print('%s \t Error \n ' %(ip))


# 实现SSH远程访问服务器，命令交互的功能,要使用交互式连接
def test_ssh( ip, port, username, passwd):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip,port=port,username=username,password=passwd,timeout=5)
    channel=ssh.invoke_shell()  # 变成交互式终端
    # 回话存续期间，连接将被保持，知道输入(exit)命令退出
    command="date"
    print("%s连接成功,请输入命令" % ip)
    while command!="exit":
        command=input(">>")
        channel.send(command+"\n")
        time.sleep(1)
        buf=channel.recv(10024).decode("utf-8")
        print(buf)
    print("bye!")
    ssh.close()


# 测试ftp文件传输功能
def test_ftp(ip,port,username,password):
    transport=paramiko.Transport((ip,port))
    transport.connect(username=username,password=password)
    sftp=paramiko.SFTPClient.from_transport(transport)
    #文件上传
    sftp.put('one.txt','/home/wll/ll/one_new.txt')
    # sftp.get('/home/wll/ll/one.txt','one.txt')
    transport.close()


if __name__ == '__main__':
    ip1, port1, username1, passwd1 = '192.168.133.129', 22, "wll", "wll"
    # test_ssh(ip1, port1, username1, passwd1)
    test_ftp(ip1, port1, username1, passwd1)







