import re
p = "[A-Z]"
s = "SLCpython123DEMO8AUG"
n = re.subn(p, '#', s)
# print(type(n))
# print(n)
print('Result string: ', n[0])
print('Num of replacements : ', n[1])
