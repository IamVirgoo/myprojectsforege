def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n + 3, end) + f(n + 6, end)


print(f(1, 8) * f(8, 11) * f(11, 14))