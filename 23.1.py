def f(n):
    if n > 25: return 0
    if n == 25: return 1
    return f(n + 1) + f(n * 3) + f(n * 4)


print(f(1))
