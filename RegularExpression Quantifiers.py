import re
pattern = "a"
pattern = "a+" # atleast one a
pattern = "a*" # any number of a available
pattern = "a{2}"
pattern = "a{1,2}"
matcher = re.finditer(pattern, "abaabaab")
for match in matcher:
    print(match.start(), match.end(), match.group())