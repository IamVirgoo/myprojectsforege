def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n > 1:
        return f(n - 1) * f(n - 2) + 1


print(f(5))