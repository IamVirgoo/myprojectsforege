count = 0
a = []
for i in range(100000, 300001):
    if i // 100 % 10 == 5 and (i % 20 == 0 or i % 25 == 0 or i % 33 == 0):
        a.append(i)
        count += 1
print(count, max(a))