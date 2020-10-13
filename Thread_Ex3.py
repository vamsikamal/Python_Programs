from threading import *
import time
def doublethenumber(numbers):
    for i in numbers:
        time.sleep(2)
        print('Double ', 2 * i)

def squareofthenumber(numbers):
    for i in numbers:
        time.sleep(2)
        print('Square ', i * i)
        
nums = [1,2,3,4,5,6,7,8,9,10]
begin = time.time()
t1 = Thread(target=doublethenumber, args=(nums, ))
t2 = Thread(target=squareofthenumber, args=(nums, ))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Time taken to execute: ', end - begin)

