def divCount(n):
    d = 2
    k = 0
    a = []
    while d ** 2 < n:
        if n % d == 0:
            a.append(d)
            a.append(n // d)
            k += 2
        d += 1
    if d ** 2 == n:
        k += 1
    if k == 4:
        a.sort()
        print(*a)


for n in range(126849, 126872):
    divCount(n)
