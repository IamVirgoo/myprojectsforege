def f(n):
    if n > 23:
        return 0
    if n == 23:
        return 1
    return f(n + 1) + f(n * 2) + f(n * 4)


print(f(2))