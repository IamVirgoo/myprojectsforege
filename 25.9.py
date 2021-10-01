def isSimple(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


k = 0
for n in range(2532000, 2532161):
    iss = isSimple(n)
    if n % 10 == 7 and iss:
        k += 1
        print(k, n)
