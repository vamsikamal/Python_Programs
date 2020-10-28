import re
s = "sunday;monday;tuesday;wednesday;thursday"
l = re.split(";", s)
print(l)
for i in l:
    print(i)