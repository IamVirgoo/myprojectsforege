s = 93 * '8'
while s.find('88888') != -1 or s.find('5555') != -1:
    if s.find('88888') != -1:
        s = s.replace('88888', '555', 1)
    else:
        s = s.replace('5555', '88', 1)
print(s)