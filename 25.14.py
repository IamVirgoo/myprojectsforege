def max_div(n):
    for el in range(n // 2, 1, -1):
        if n % el == 0:
            return el


def min_div(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return i
    return 0


delitsa = 3
count = 0
x = 300001
while count < 5:
    dmax, dmin = max_div(x), min_div(x)
    if dmin and dmax and dmax != dmin and (dmax - dmin) % delitsa == 0:
        count += 1
        print(x, (dmax - dmin))
    x += 1
