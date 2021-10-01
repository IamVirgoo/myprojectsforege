with open('D:/k7-0.txt', 'r') as f:
    s = f.readline()

max_len = 0
c_len = 0
for c in s:
    if c == 'C':
        c_len += 1
        if c_len > max_len:
            max_len = c_len

print(max_len)
