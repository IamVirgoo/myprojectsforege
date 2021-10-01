s = 123 * '1'
while s.find('1111') != -1 or s.find('888') != -1:
    if s.find('1111') != -1:
        s = s.replace('1111', '88', 1)
    else:
        s = s.replace('888', '1', 1)
print(s)