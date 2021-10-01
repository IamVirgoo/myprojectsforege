s = 191 * '2'
while s.find('7777') != -1 or s.find('22222') != -1:
    if s.find('7777') != -1:
        s = s.replace('7777', '22', 1)
    else:
        s = s.replace('22222', '777', 1)
print(s)