for el in range(1, 100001):
    x = el
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 == 1:
            m += x % 10
        x //= 10
    if l == 4 and m == 13:
        print(el)
