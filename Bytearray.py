# Bytearray is similar to bytes but we can modify elements

ba = bytearray([10,20,30])
print(ba)
print(type(ba))

ba[1] = 200
for i in ba:
    print(i)