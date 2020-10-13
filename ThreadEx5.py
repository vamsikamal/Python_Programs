from threading import *

class Test:
    def display(self, name, course):
        for i in range(10):
            print(i)

obj = Test()
t = Thread(target=obj.display, args=('slc','Python',))
t.start()
