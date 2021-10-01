def maxdiv(n):
    for el in range(n // 2, 1, -1):
        if n % el == 0:
            return el


def mindiv(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return i
    return 0


count, n = 0, 850001
delitsa = 7
while count < 6:
    dmin, dmax = mindiv(n), maxdiv(n)
    if dmin and dmax and dmin != dmax and (dmax - dmin) % delitsa == 0:
        count += 1
        print(n, dmax - dmin)
    n += 1
