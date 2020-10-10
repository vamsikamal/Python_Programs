from threading import *
from time import *

def display():
    for i in range(10):
        sleep(1)
        print('display method')

def display2():
    for i in range(10):
        sleep(1)
        print('display2 method')


t = Thread(target=display)
t.start()
t1 = Thread(target=display2)
t1.start()

print('End of the program')