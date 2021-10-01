s = 100 * '7'
while s.find('7777') != -1 or s.find('222') != -1:
    if s.find('7777') != -1:
        s = s.replace('7777', '22')
    else:
        s = s.replace('222', '7')
print(s)