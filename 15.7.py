k = 0
for a in range( 1, 1000):
    ok = 1
    for x in range(1, 100):
        for y in range(1, 100):
            ok *= (not(x > 8) or (x * x + 3 * x >= a) and (not(y * y + 5 * y > a) or (y >= 4)))
            if not ok:
                break
    if ok:
        k += 1
print(k)