def divCount(n):
    d = 1
    k = 0
    while d * d < n:
        if n % d == 0:
            k += 2
        d += 1
    if d * d == n:
        k += 1
    return k

def secondmaxDiv(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return x // d
        d += 1


max_ = -1
for n in range(394441, 394506):
    k = divCount(n)
    if k > max_:
        max_ = k
        x = n
y = secondmaxDiv(x)

print(max_, y, n)
