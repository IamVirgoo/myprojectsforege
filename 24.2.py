with open('D:/Решение 24-го/24-3.txt', 'r') as f:
    s = f.readline()

max_len = 1
c_len = 1
c = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c_len += 1
        if c_len > max_len:
            max_len = c_len
        else:
            c_len = 1
print(max_len)