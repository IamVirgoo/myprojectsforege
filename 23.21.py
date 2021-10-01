def f(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    return f(n + 1, end) + f(n + 2, end) + f(n + 4, end)


print(f(3, 17) * f(17, 21) * f(21, 23))