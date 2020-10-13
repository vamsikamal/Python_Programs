from threading import *
import time

s = Semaphore(3)

def wish(name):
    s.acquire()
    for i in range(10):
        print('Good morning', end='')
        time.sleep(2)
        print(name)
    s.release()

t1 = Thread(target=wish, args=('USER1',))
t2 = Thread(target=wish, args=('USER2',))
t3 = Thread(target=wish, args=('USER3',))
t4 = Thread(target=wish, args=('USER4',))
t5 = Thread(target=wish, args=('USER5',))
t6 = Thread(target=wish, args=('USER6',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()