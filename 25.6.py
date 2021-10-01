def maxDiv(x):
    d = 2
    while d * d < x:
        if x % d == 0:
            return x // d
        d += 1
    return 0


def isSimple(x):
    if x == 1: return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


k = 0
x = 550001
while k < 6:
    d = maxDiv(x)
    if d != 0 and not isSimple(d):
        print(x, d)
        k += 1
    x += 1
