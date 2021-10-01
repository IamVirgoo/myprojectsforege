# (not(Del(x, a) and dell(x, 3)) -> not(dell(x, 4)
# Найти наибольшее a для которого формула тождественно истина

for a in range(1000, 0, -1):
    flag = 0
    for x in range(1, 1001):
        if not(((x % a != 0) and (x % 3 == 0)) <= (x % 4 != 0)):
            flag = 1
            break
    if flag == 0:
        print(a)
