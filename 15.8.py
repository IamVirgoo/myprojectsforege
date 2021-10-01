k = 0
for a in range(1, 1000):
    ok = 1
    for x in range(1, 100):
        for y in range(1, 100):
            ok *= (not(x >= 11) or (x * x + 2 * x > a) and (not(y * y + 3 * y >= a) or (y > 8)))
            if not ok:
                break
    if ok:
        k += 1
print(k)
