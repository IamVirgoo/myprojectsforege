def s(n):
    s = 0
    k = 0
    for el in range(2, (n // 2)+1):
        if n % el == 0:
            k += 1
    if k == 2:
        s += el
        return s
    return 0


print(s(10))
count, x = 0, 1000001
while count < 5:
    if s(x) and s(x) % 10 == 3:
        count += 1
        print(x, s(x))
    x += 1
