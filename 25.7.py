def calcS(x):
    d = 2
    s = 0
    while x > 1:
        if x % d == 0:
            s += d
            while x % d == 0:
                x //= d
        d += 1
    return s


k = 0
x = 650001
while k < 5:
    s = calcS(x)
    if s % 10 == 3:
        print(x, s)
        k += 1
    x += 1
