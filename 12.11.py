s = (131 * '3') + (131 * '7')
while s.find('3333') != -1:
    s = s.replace('3333', '7', 1)
    s = s.replace('7777', '3', 1)
print(s)