a = 10
def test():
    global a
    print(a)

def test2(b):
    a = b
    print(a)

test()
test2(50)
print(a)

