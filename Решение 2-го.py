# (z -> x) ^ (x = не w) ^ (w or y)
print('x', 'y', 'z', 'w')
for z in range(2):
    for x in range(2):
        for w in range(2):
            for y in range(2):
                if (z <= x) and (x == (not(w))) and (w or y):
                    print(x, y, z, w)