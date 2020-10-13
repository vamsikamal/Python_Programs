from threading import *
import time
def doublethenumber(numbers):
    f = open('double.txt','w')
    for i in numbers:
        time.sleep(2)
        f.write(str(2 * i))
        f.write('\n')
    print('Double the numbers is executed.')
    f.close()

def squareofthenumber(numbers):
    f = open('square.txt', 'w')
    for i in numbers:
        time.sleep(2)
        f.write(str(i * i))
        f.write('\n')
    f.close()
    print('Square the number is executed')

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

