
s = (1 * '1') + (110 * '0')
while s.find('10000') != -1 or s.find('1') != -1:
    if s.find('10000') != -1:
        s = s.replace('10000', '001', 1)
    else:
        s = s.replace('1', '00000')
print(s)

