def min_div(n, start=2):
    if n % start == 0:
        return 2
    for i in range(3, n // 2, 2):
        if n % i == 0 and isSimple(i):
            return i
    return 0


def isSimple(x):
    if x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


n, count = 750001, 0
delitsa = 8
while count < 5:
    m1 = min_div(n)
    if m1 == 0:
        continue
    m2 = min_div(n, m1 + 1)
    print(n, m1, m2, m1+m2)
    if m2 and (m1 + m2) % delitsa == 0:
        count += 1
        print(n, m1 + m2)
    n += 1
