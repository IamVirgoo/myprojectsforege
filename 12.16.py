s = 101 * '1'
while s.find('1111') != -1 or s.find('222') != -1:
    if s.find('1111') != -1:
        s = s.replace('1111', '22', 1)
    else:
        s = s.replace('222', '1', 1)
print(s)
