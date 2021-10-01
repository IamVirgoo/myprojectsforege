def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n + 3, end) + f(n + 4, end)


print(f(4, 12) * f(12, 15) * f(15, 19))