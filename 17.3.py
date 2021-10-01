count = 0
a = []
for i in range(300000, 600001):
    if ((i % 10) == 5 or (i % 10) == 2) and (i // 10 % 10) != 4 and (i % 17) == 0:
        a.append(i)
        count += 1

print(count, max(a))
