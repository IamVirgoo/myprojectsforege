count = 0
a = []
for i in range(2000, 100001):
    if i % 53 == 0 and i % 37 != 0 and i % 11 != 0 and i % 7 != 0 and i % 19 != 0:
        a.append(i)
        count += 1
print(count, min(a))