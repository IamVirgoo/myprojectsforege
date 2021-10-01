def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n + 3, end) + f(n * 2, end)


print(f(3, 11) * f(11, 17))
