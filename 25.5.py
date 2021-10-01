def calcF(n):
    d = 2
    while d ** 2 < n:
        if n % d == 0:
            return n // d - d
        d += 1
    return 0


k = 0
n = 850001
while k < 6:
    f = calcF(n)
    if f != 0 and f % 7 == 0:
        k += 1
        print(n, f)

    n += 1
