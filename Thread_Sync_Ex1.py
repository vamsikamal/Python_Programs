from threading import *
import time
l = Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('Good morning ', end='')
        time.sleep(2)
        print(name)
    l.release()


t1 = Thread(target=wish, args=('SLC', ))
t2 = Thread(target=wish, args=('PYTHON', ))

t1.start()
t2.start()
