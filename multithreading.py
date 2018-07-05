#author_by zhuxiaoliang
#2018-07-04 下午7:15

"""
GIL全局解释锁
同一时刻同一进程中只能有一个线程被执行

"""

import time
import threading


def text(name):
    def profile(func):
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            end = time.time()
            print("{}cost:{}".format(name,end-start))
            return res
        return wrapper
    return profile


def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

@text('nothread')
def nothread():
    fib(3)
    fib(3)

@text('hasthread')
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib,args=(3,))
        t.start()
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            #print(t)
            if t is main_thread:
                continue
            t.join()
nothread()
hasthread()