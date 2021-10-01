def divisors(n):
    d = 1
    k = 0
    a = []
    while d ** 2 < n:
        if n % d == 0:
            if d % 2 != 0:
                a.append(d)
                k += 1
            if n // d % 2 != 0:
                a.append(n // d)
                k += 1
        d += 1
    if d ** 2 == n:
        if d % 2 != 0:
            a.append(d)
            k += 1

    if k == 4:
        a.sort()
        print(*a)


for n in range(190061, 190081):
    divisors(n)
