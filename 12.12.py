s = (80 * '7') + (80 * '8')
while s.find('7777') != -1:
    s = s.replace('7777', '8', 1)
    s = s.replace('8888', '7', 1)
print(s)