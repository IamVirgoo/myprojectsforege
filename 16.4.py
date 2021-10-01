def f(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return f(n-2) * (n-1) + 2


print(f(8))