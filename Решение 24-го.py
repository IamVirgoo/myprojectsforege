# Самая длинная цепочка символов 'C'

''' with open('Расположение', 'r') as f:
    s = f.readline()

max_len = -100
c_len = 0
for c in s:
    if c == 'c':
        c_len += 1
        if c_len > max_len:
            max_len = c_len
    else:
        c_len = 0 '''

# Самая длинная цепочка любых символов

'''with open('D:\input1.txt', 'r') as f:
    s = f.readline()

max_len = 1
c_len = 1
c = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c_len += 1
        if c_len > max_len:
            max_len = c_len
            c = s[i]
        else:
            c_len = 1

print(max_len)'''


# Максимальное кол-во идущих подряд символов в алфавитном порядке

'''with open('Расположение', 'r') as f:
    s = f.readline()
k = 1
maxx = 0
for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 1


print(maxx)'''

# Найти максимальное количество идущих подряд символов, среди которых  нет символа "Z"

'''with open('Расположение', 'r') as f:
    s = f.readline()
k = 0
maxx = 0
for i in range(len(s)):
    if s[i] != 'Z':
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 0


print(maxx)'''

# Найти максимальное количество идущих подряд символов, среди которых "Z" встречается не более одного раза

"""with open('Расположение', 'r') as f:
    s = f.readline()
a = []
for i in range(len(s)):
    if s[i] == 'Z':
        a.append(i)
a.append(len(a))

max_ = -1
for i in range(len(a) - 2):
    k = a[i + 2] - a[i] - 1
    if k > max_:
        max_ = k

print(k)"""

# Задание 33 в листке

"""with open("D:/Решение 24-го/24data/k7data/k7c-1.txt", 'r') as f:
    s = f.readline()
count = 0
for el in range(len(s) - 2):
    if s[el] in 'BCD':
        if s[el + 1] in 'BDE' and s[el + 1] != s[el]:
            if s[el + 2] in 'BCE' and s[el + 2] != s[el + 1]:
                count += 1
print(count)"""

# Задание 34 в листке

'''with open("D:/Решение 24-го/24data/k7data/k7c-2.txt", 'r') as f:
    s = f.readline()
count = 0
for el in range(len(s) - 2):
    if s[el] in 'ACE':
        if s[el + 1] in 'ADF' and s[el + 1] != s[el]:
            if s[el + 2] in 'ABF' and s[el + 2] != s[el + 1]:
                count += 1
print(count)'''

# Задача 61 в листке

'''with open("D:/Решение 24-го/24data/k8data/k8-52.txt", 'r') as f:
    s = f.readline()
count = 1
maxx = 1
c = s[0]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
        if count > maxx:
            maxx = count
            c = s[i]
    else:
        count = 1
print(maxx, c)'''

# Задача 62 в листке

'''with open("D:/Решение 24-го/24data/k8data/k8-55.txt", 'r') as f:
    s = f.readline()
count = 1
maxx = 1
c = s[0]
for el in range(1, len(s)):
    if s[el] == s[el - 1]:
        count += 1
        if count > maxx:
            maxx = count
            c = s[el]
    else:
        count = 1
print(maxx, c)'''


# Символ, который чаще всего встречается после А

"""with open('', 'r') as f:
    s = f.readline()
a = [0] * 26
for i in range(len(s) - 1):
    if s[i] == 'A':
        c = s[i + 1]
        a[ord(c) - ord('A')] += 1
max_ = 0
for i in range(26):
    if a[i] >= max_:
        max_ = a[i]
        best = chr(ord('A') + i)
print(best)"""
