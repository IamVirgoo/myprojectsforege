def f(n):
    if n == 1:
        return 2
    if n > 1:
        return f(n-1) * (2*n-1)


print(f(5))