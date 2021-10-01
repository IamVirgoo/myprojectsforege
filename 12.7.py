s = 78 * '2'
while s.find('222222') != -1:
    s = s.replace('5555', '2', 1)
    s = s.replace('2222', '5', 1)
print(s)