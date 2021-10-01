s = 113 * '4'
while s.find('4444') != -1 or s.find('1111') != -1:
    if s.find('4444') != -1:
        s = s.replace('4444', '1', 1)
    else:
        s = s.replace('1111', '4', 1)
print(s)