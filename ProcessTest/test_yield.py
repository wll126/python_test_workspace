#!/usr/bin/python3
# coding:utf8

"""
测试协程的方法 测试时间 2019年08月14日
yield
"""

def test1():
    b='1'
    a = yield 5
    print("print a",a)
    f=yield 16
    print("print f:%s" %f)

def test2():
    pass

def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

def test():
    for i in fab(5):
        print(i)

if __name__=="__main__":
    c=test1()
    d1=next(c)
    print("d1=",d1)
    r2=c.send('good luck')
    print("r2=",r2)
    # d2=next(c)

