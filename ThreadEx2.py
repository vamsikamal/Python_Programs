from threading import *
from time import *

class Test:
    def display(self):
        for i in range(10):
            sleep(1)
            print('Child Thread')


print(current_thread().name)
t = Thread(target=display)
t.start()

for i in range(10):
    sleep(1)
    print('Main Thread')