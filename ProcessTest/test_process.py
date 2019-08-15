# coding=utf8

import os,time,random
from multiprocessing import Process,Pool

print("process (%s) start .." % os.getpid())

def run_proc(name):
    print('Run child process %s .(%s)' % (name,os.getpid()))

def long_time_task(name):
    print("run task %s(%s)" %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("task %s runs %0.2f seconds " %(name,end-start))


if __name__=="__main__":
    print("parent process is :%s" %os.getpid())
    q=Pool(4)
    for i in range(6):
        q.apply_async(long_time_task,args=(i,))
    print("waiting for all subprocesses done ...")
    q.close()
    q.join()
    print("all subprocesses done")
    # p=Process(target=run_proc, args=("test",))
    # print("child process will start")
    # p.start()
    # p.join()    # 同步
    # print('Child process end.')



#
# print(os)
# pid=os.fork()
# if pid==0:
#     print("I am a child process  (%s),and my parent process is (%s)" %(os.getpid(),os.getppid()))
# else:
#     print("I (%s) just created a child process %s" %(os.getpid(),pid))

