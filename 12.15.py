s = (64 * '9') + (64 * '5')
while s.find('999') != -1:
    s = s.replace('999', '5', 1)
    s = s.replace('555', '9', 1)
print(s)