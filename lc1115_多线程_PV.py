# Title     : lc1115_多线程_PV.py
# Created by: julse@qq.com
# Created on: 2021/8/25 22:26
# des : TODO
import _thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = False
        self.s2 = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            while self.s1: pass
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.s2 = False
            self.s1 = True

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            while self.s2: pass
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.s1 = False
            self.s2 = True
def printFoo():
    print('foo', end='')
def printBar():
    print('bar', end='')
# 创建两个线程
fb = FooBar(3)
try:
   _thread.start_new_thread(fb.foo,(printFoo,))
   _thread.start_new_thread(fb.bar,(printBar,))

except:
    print("Error: unable to start thread")

while 1:pass

#
# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#
# while 1:
#    pass