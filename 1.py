def cointStep(x, y):
    if x + y >= win:
        return 0
    else:
        return a[x][y]


win = 76
s1 = 3

a = []
for i in range(win):
    a.append([0] * win)


for i in range(win - 1, -1, -1):
    for j in range(win - 1, -1, -1):
        if i + j >= win:
            a[i][j] = 0
        else:
            s = [cointStep(i + 3, j), cointStep(i, j + 3), cointStep(i * 3, j), cointStep(i, j * 3)]


            minEven = 1000
            maxOdd = -1000
            for el in s:
                if el % 2 == 0 and el < minEven:
                    minEven = el
                if el % 2 != 0 and el > maxOdd:
                    maxOdd = el
            if minEven != 1000:
                a[i][j] = minEven + 1
            else:
                a[i][j] = maxOdd + 1

for j in range(1, win):
    if a[s1][j] == 1:
        print(j, end=' ')
print()
for j in range(1, win):
    if a[s1][j] == 2:
        print(j, end=' ')
print()
for j in range(1, win):
    if a[s1][j] == 3:
        print(j, end=' ')
print()
for j in range(1, win):
    if a[s1][j] == 4:
        print(j, end=' ')
print()
for j in range(1, win):
    s = [cointStep(s1 + 3, j), cointStep(s1, j + 3), cointStep(s1 * 3, j), cointStep(s1, j * 3)]
    if 1 in s:
        print(j, end=' ')
print()