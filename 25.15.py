def max_div(n):
    for el in range(n // 2, 1, -1):
        if n % el == 0:
            return el


def min_div(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return i


x, count, dell = 400001, 0, 7
while count < 5:
    dmin, dmax = min_div(x), max_div(x)
    if dmin and dmax and dmax != dmin and (dmax - dmin) % dell == 0:
        count += 1
        print(x, (dmax - dmin))
    x += 1
