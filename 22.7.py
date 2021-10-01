for el in range(1, 100000001):
    x = el
    a = 0
    b = 1
    while x > 0:
        a += 2
        b *= x % 100
        x //= 100
    if a == 4 and b == 160:
        print(el)