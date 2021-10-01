f = ("D:\Решение 26-го\26\input26_13.txt")

q, n = map(int, f.readline().split())

a = []
for i in range(n):
    a.append(int(f.readline()))
a.sort()

s = 0
i = -1
while s <= q:
    i += 1
    s += a[i]
s -= a[i]
result1 = i
s -= a[i - 1]
free = q - s

i -= 1
while a[i] <= free:
    i += 1

i -= 1
result2 = a[i]
print(result1, result2)