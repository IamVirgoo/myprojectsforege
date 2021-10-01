def f(n, end, ex):
    if n > end:
        return 0
    if n == ex:
        return 0
    if n == end:
        return 1
    return f(n + 1, end, ex) + f(n * 2, end, ex)


print(f(3, 15, 26) * f(15, 36, 26))