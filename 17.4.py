count = 0
a = []
for i in range(300000, 600001):
    if ((i % 10) == 6 or (i % 10) == 0) and (i // 10 % 10) != 6 and i % 31 == 0:
        a.append(i)
        count += 1
print(count, max(a))