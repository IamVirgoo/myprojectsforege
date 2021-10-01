def div(n):
    a = []
    for el in range(1, n+1):
        if n % el == 0 and el % 2 != 0:
            a.append(el)
    return a


for n in range(351870, 351881):
    if len(div(n)) == 4:
        print(n, *div(n))
