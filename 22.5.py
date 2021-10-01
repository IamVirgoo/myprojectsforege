for el in range(1, 1000001):
    x = el
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 10
        x //= 10
    if a == 3 and b == 54:
        print(el)