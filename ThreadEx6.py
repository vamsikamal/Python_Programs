from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print(i)

t = MyThread()
t.start()