def f(n, end, ex):
    if n > end:
        return 0
    if n == ex:
        return 0
    if n == end:
        return 1
    return f(n + 1, end, ex) + f(n * 2, end, ex)


print(f(1, 15, 28) * f(15, 41, 28))