count = 0
a = []
for i in range(1845, 99999+1):
    if i % 7 != 0 and i % 25 > 15 and i % 10 == i // 10 % 10:
        a.append(i)
        count += 1
print(count, sum(a))