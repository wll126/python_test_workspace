# coding:utf8
"""
生产者和消费者  多进程+协程实现
"""

# 消费者
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return

        print("Consumer %s consuming  " % n)
        r='200 OK'

# 生产者
def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print("producing is %s" % n)
        r=c.send(n)
        print("[PRODUCER] Consumer return is %s" % r)
    c.close()

c=consumer()
produce(c)
