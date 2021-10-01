s = 156 * '4'
while s.find('444444') != -1 or s.find('888') != -1:
    if s.find('444444') != -1:
        s = s.replace('444444', '8888', 1)
    else:
        s = s.replace('888', '4', 1)
print(s)