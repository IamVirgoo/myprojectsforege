for el in range(1, 100000001):
    x = el
    a, b = 0, 0
    while x > 0:
        a += 1
        b += x % 100
        x //= 100
    if a == 2 and b == 78:
        print(el)
