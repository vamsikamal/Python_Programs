import re

pattern = "\s" # space
pattern = "\S" # except space
pattern = "\d" # digits
pattern = "\D" # except digits
pattern = "\w" # word character, alpha numerics
pattern = "\W" # Except word characters, or special characters
pattern = "."  # all characters will be considered 

matcher = re.finditer(pattern, "a7b@k 9zADBC")
for match in matcher:
    print(match.start(), match.end(), match.group())