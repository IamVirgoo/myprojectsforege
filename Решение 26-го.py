with open("D:/Решение 26-го/26/input26_13.txt", 'r') as f:
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.rstrip())

s = int(lines[0].split()[0])
lines = [int(lines[i]) for i in range(1, len(lines))]
lines = sorted(lines)
n = len(lines)

max_len = 0
summ = 0
for i in lines:
    if summ + i <= s:
        summ += i
        max_len += 1
print(max_len, end=' ')

for i in range(n - 1, -1, -1):
    summ = lines[i]
    count = 0
    for j in range(n):
        if summ + lines[j] <= s:
            count += 1
            summ += lines[j]
    if max_len == count + 1:
        break


print(lines[i])