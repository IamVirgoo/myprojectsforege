for el in range(1, 100001):
    x = el
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0: a += 1
        else: b += 1
        x //= 6
    if a == 3 and b == 0:
        print(el)