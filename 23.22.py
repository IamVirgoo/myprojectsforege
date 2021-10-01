def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n * 2 + 1, end)


print(f(1, 4) * f(4, 26))