for n in range(190061, 200001):
    d = 1
    k = 0
    a = []
    f = 0
    while d ** 2 < n:
        if n % d == 0:
            if d % 2 != 0 and n // d % 2 != 0:
                a.append(d)
                a.append(n // d)
                k += 2
            else:
                f = 1
        d += 1
    if d ** 2 == n:
        if d % 2 != 0:
            a.append(d)
            k += 1
        else:
            f = 1

    if k == 4 and f == 0:
        a.sort(reverse=True)
        print(*a)
