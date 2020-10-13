from threading import *
l = RLock()

l.acquire()
print('Main thread : LOCKED')

l.acquire()
print('Main thread : LOCKED')
l.release()
print('Main thread : RELEASED THE LOCK')