# Две команды: +1, *3, *4
# Сколько программ, которые преобразуют число 2 в 22

print('№1')

def f(n):
    if n > 22: return 0
    if n == 22: return 1
    return f(n + 1) + f(n * 3) + f(n * 4)


print(f(2))
print()

# + 2, + 4. Из 3 в 19, содержит ровно одно из 10 и 9

print('№2')
def f1(n, end, ex):
    if n > end: return 0
    if n == ex: return 0
    if n == end: return 1
    return f1(n + 2, end, ex) + f1(n + 4, end, ex)


print(f1(3, 10, 9) * f1(10, 19, 9), f1(3, 9, 10) * f1(9, 19, 10))

