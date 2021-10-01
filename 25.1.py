def func(n):
    d = 2
    k = 0
    while d ** 2 < n:
        if n % d == 0:
            a = d
            b = n // d
            k += 2
        d += 1
    if d ** 2 == n:
        k += 1
    if k == 2:
        print(a, b)


for n in range(174457, 174506):
    func(n)
