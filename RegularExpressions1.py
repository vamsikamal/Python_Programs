# re used to find a pattern
import re
pattern = re.compile("ab")
matcher = pattern.finditer("abaababa")
counter = 0

#print(type(matcher))
for match in matcher:
    #print(type(match))
    print(match.start(), match.end(), match.group())
    counter = counter + 1

print('Number of matches found: ', counter)


