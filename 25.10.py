def digitSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def digitP(n):
    p = 1
    while n > 0:
        p *= n % 10
        n //= 10
    return p


for n in range(87921, 88187):
    if digitSum(n) % 14 == 0 and digitP(n) % 18 == 0 and digitP(n) != 0:
        print(digitSum(n), digitP(n))