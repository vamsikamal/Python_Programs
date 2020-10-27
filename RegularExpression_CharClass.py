import re
# pattern = "[abc]"   # checks for matching a or b or c
#pattern = "[^abc]"    # checks for characters except a and b and c
#pattern = "[a-z]"     # considers all lower case alphabets
#pattern = "[A-Z]"     # considers all upper case alphabets
#pattern = "[0-9]"     # considers only numbers
#pattern = "[a-zA-Z]"  # considers alphabets
#pattern = "[a-zA-Z0-9]" # alpha numerics are considered
pattern = "[^a-zA-Z0-9]" # Except alpha numberics, i.e, special characters

matcher = re.finditer(pattern, "a7b@k9zADBC")
for match in matcher:
    print(match.start(), match.end(), match.group())