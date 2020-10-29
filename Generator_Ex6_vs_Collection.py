import random
import time

names = ['Ramesh','Rajesh','Kumar','sahasra','Anwitha']
subject = ['Python','Java','CSharp','ASP','VB','Django']

def GetFromList(num):
    result = []
    for i in range(num):
        p = {'id':i, 'name':random.choice(names), 'subject':random.choice(subject)}
        result.append(p)
    return result

def GetFromYield(num):
    for i in range(num):
        p = {'id':i, 'name':random.choice(names), 'subject':random.choice(subject)}
        yield p

t1 = time.time()
l1 = GetFromList(10000)
t2 = time.time()
print('Time taken for GetFromList: ', t2 - t1)


t1 = time.time()
l1 = GetFromYield(10000)
t2 = time.time()
print('Time taken for GetFromYield: ', t2 - t1)