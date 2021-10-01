def f(n, end, ex):
    if n > end:
        return 0
    if n == end:
        return 1
    if n == ex:
        return 0
    return f(n + 1, end, ex) + f(n * 2, end, ex)


print(f(2, 16, 29) * f(16, 42, 29))