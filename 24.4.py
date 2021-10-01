with open("D:/Решение 24-го/24data/k7data/k7a-6.txt", 'r') as f:
    s = f.readline()

max_l = 0
c_len = 0
for c in s:
    if c not in 'AE':
        c_len += 1
        if c_len > max_l:
            max_l = c_len
    else:
        c_len = 0
print(max_l)
