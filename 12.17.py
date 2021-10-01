s = (71*'9') + (71*'3')
while s.find('9999') != -1:
    s = s.replace('9999', '3', 1)
    s = s.replace('3333', '9', 1)
print(s)
