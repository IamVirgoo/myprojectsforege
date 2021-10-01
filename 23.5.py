def f(n):
    if n > 33:
        return 0
    if n == 33:
        return 1
    return f(n + 1) + f(n * 2) + f(n * 3)


print(f(3))