s = 83 * '1'
while s.find('11111') != -1:
    s = s.replace('11111', '3', 1)
    s = s.replace('3333', '1', 1)
print(s)