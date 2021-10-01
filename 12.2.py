s = (51 * '5') + (51 * '4')
while s.find('555') != -1:
    s = s.replace('555', '4', 1)
    s = s.replace('444', '5', 1)
print(s)