count = 0
a = []
for i in range(100000, 300001):
    if i // 100 % 10 == 0 and (i % 17 == 0 or i % 50 == 0 or i % 47 == 0):
        a.append(i)
        count += 1
print(count, max(a))