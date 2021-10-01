def f(n):
    if n == 1:
        return 3
    if n > 1:
        return f(n-1) * (2*n-2)


print(f(5))