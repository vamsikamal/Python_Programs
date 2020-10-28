import re
s = input('Enter pattern to check : ')
m = re.match(s, "abcabdefg")   # starts with
if m != None:
    print('Match found: ', m.start(), m.end(), m.group())
else:
    print('Match not found')