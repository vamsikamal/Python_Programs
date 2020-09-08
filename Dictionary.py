# Dictionary contains elements as key value pairs

# Dictionary
dict = {'Name':'SLC', 'Location':'Hyd', 'Course':'Python', 'Fee':3000}
print(type(dict))
print(dict)

print(dict['Location'])       # 'Hyd
print(dict.get('Location'))   # 'Hyd

# Add new element
dict['Pin'] = 554433
print(dict)            # {'Name': 'SLC', 'Location': 'Hyd', 'Course': 'Python', 'Fee': 3000, 'Pin': 554433}

# Update element
dict['Pin'] = 110022
print(dict)          # {'Name': 'SLC', 'Location': 'Hyd', 'Course': 'Python', 'Fee': 3000, 'Pin': 110022}

# Remove
del dict['Pin']
print(dict)         # {'Name': 'SLC', 'Location': 'Hyd', 'Course': 'Python', 'Fee': 3000}

# Pop
t = dict.popitem()
print(t)            # ('Fee', 3000)
print(dict)         # {'Name': 'SLC', 'Location': 'Hyd', 'Course': 'Python'}

t = dict.pop('Course')
print(t)            # Python
print(dict)         # {'Name': 'SLC', 'Location': 'Hyd'}


dict = {'Name':'SLC', 'Location':'Hyd', 'Course':'Python', 'Fee':3000}
for k in dict.keys():
    print(k)

for k in dict.keys():
    print(k, dict[k])

for v in dict.values():
    print(v)

for k,v in dict.items():
    print(k,v)