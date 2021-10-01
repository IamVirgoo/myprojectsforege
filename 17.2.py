count = 0
a = []
for i in range(2000, 100001):
    if i % 19 == 0 and i % 13 == 0 and i % 3 == 0 and i % 47 != 0:
        a.append(i)
        count += 1
print(count, min(a))
