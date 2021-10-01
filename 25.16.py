def max_div(n):
    for el in range(n // 2, 1, -1):
        if n % el == 0:
            return el


def isPrime(n):
    k = 0
    for i in range(1, n + 1):
        if n % i == 0: k += 1
    if k == 2:
        return True
    else:
        return False


count, x = 0, 600001
while count < 5:
    if max_div(x) != x and not isPrime(x):
        count += 1
        print(x, max_div(x))
    x += 1
