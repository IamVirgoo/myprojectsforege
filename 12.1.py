s = 146 * '2'
while s.find('2222') != -1 or s.find('888') != -1:
    if s.find('2222') != -1:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('888', '2', 1)
print(s)
