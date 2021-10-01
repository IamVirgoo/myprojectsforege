s = 141 * '8'
while s.find('8888') != -1 or s.find('222') != -1:
    if s.find('8888') != -1:
        s = s.replace('8888', '22', 1)
    else:
        s = s.replace('222', '8', 1)
print(s)