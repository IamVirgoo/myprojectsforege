def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) * (2*n-3)


print(f(4))