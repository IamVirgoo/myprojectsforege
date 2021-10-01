s = 101 * '761'
while s.find('76') != -1 or s.find('1111') != -1:
    s = s.replace('76', '1', 1)
    s = s.replace('1111', '1', 1)
print(s)