def g(n):
    if n == 1:
        return 1
    if n > 1:
        return -f(n-1) - 2 * g(n-1)
    if n:
        return 3 * f(n-1) -4 * g(n-1)


def f(n):
    if n == 1:
        return 1
    if n:
        return 3 * f(n - 1) - 4 * g(n - 1)


print(f(7) - g(7))