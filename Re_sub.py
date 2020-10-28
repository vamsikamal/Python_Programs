import re
p = "[A-Z]"
s = "SLCpython123DEMO8AUG"
s = re.sub(p, '#', s)
print(s)


