for el in range(1, 10000001):
    x = el
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 8
        x //= 8
    if a == 4 and b == 216:
        print(el)
