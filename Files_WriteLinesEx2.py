f = open('demo.txt', 'w')
list = ['sunday\n', 'monday\n', 'tuesday\n','wednesday\n']
f.writelines(list)
f.close()
print('File closed')