def f(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return 4 * f(n - 1) - 3 * f(n - 2)


print(f(6))