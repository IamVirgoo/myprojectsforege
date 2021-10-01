def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 2, end) + f(n + 4, end) + f(n + 6, end)


print(f(3, 9) * f(9, 19))