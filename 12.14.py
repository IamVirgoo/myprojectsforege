s = (78 * '9') + (78 * '8')
while s.find('9999') != -1:
    s = s.replace('9999', '8', 1)
    s = s.replace('8888', '9', 1)
print(s)