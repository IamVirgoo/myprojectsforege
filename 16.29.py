def g(n):
    if n == 1:
        return 1
    if n > 1:
        return -4 * f(n-1) - g(n-1)
    if n:
        return -2 * f(n-1) + 4 * g(n-1)


def f(n):
    if n == 1:
        return 1
    if n:
        return -2 * f(n - 1) + 4 * g(n - 1)


print(g(8) - f(8))
