k = 0
for a in range(1, 1000):
    ok = 1
    for x in range(1, 100):
        for y in range(1, 100):
            ok *= (not(x<=9) or (x**2 <= a) and (not(y**2 <= a) or (y < 10)))
            if not ok:
                break
    if ok:
        k += 1
print(k)

