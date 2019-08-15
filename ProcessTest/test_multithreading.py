# coding=utf8

import time,threading,multiprocessing

balance=0
# 任务体
def loop():
    print(" threading %s is running ." % threading.current_thread().name)
    n=1
    while True:
        n=n*(n+1)
        print("thread %s>> %s" %(threading.current_thread().name,n))
        # time.sleep(1)
    # print("thread %s is ending..." % threading.current_thread().name)

def test1():
    print("thread %s is now running ...." % threading.current_thread().name)
    t=threading.Thread(target=loop,name="LoopThread")
    t.start()
    t.join()
    print("thread %s is now ending ..." % threading.current_thread().name)

def change_it(n):
    global balance
    # 先存款后取款，余额应该不变
    balance=balance+n
    balance-=n

def run_thread(n):
    for i in range(100000):
        change_it(n)

def test2():
    t1=threading.Thread(target=run_thread,args=(5,))
    t2=threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("余额=%d" %balance)

lock=threading.Lock()

def run_add_lock(n):
    for i in range(100000):
        # 加锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release()

def test3():
    t1=threading.Thread(target=run_add_lock,args=(5,))
    t2=threading.Thread(target=run_add_lock,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("余额=%d" %balance)

def test4():
    for i in range(multiprocessing.cpu_count()):
        t=threading.Thread(target=loop)
        t.start()


if __name__=="__main__":
    test4()
