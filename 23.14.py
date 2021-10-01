def f(n, end, ex):
    if n > end:
        return 0
    if n == ex:
        return 0
    if n == end:
        return 1
    return f(n + 1, end, ex) + f(n * 3, end, ex)


print(f(3, 16, 45) * f(16, 53, 45))