s = 96 * '4'
while s.find('444') != -1 or s.find('555') != -1:
    if s.find('444') != -1:
        s = s.replace('444', '5', 1)
    else:
        s = s.replace('555', '4', 1)
print(s)