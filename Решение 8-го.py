# Сколько слов длины 3, начинающиеся с гласной буквы, можно составить из букв О, Б, А и И?
# Каждая буква может входить в слово несколько раз. Слова обязательно должны быть осмысленными словами русского языка

print('№1')
k = 0
for a in 'ОАИ':
    for b in 'ОАИБ':
        for с in 'ОАИБ':
            k += 1
print(k)
print('___________')
print()

# Шифр кодового замка представляет собой последовательность из 4 символов, каждый из которых является одной из цифр 0-8
# Сколько различных вариантов шифра можно задать, если известно, что все цифры в шифре различны

print('№2')
k = 0
for a in range(0, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(0, 9):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    k += 1
print(k)
print('___________')
print()

# Михаил составляет 5-букыенные коды.
# В кодах разрешается использовать только буквы Е, Д и К, при этом код не может начинать с глассной и не может содержать двух одинаковых букв подряд.
# Сколько различных кодов может составить Михаил.

print('№3')
word = 'ЕДК'
k = 0
for a in 'ДК':
    for b in word:
        for c in word:
            for d in word:
                for e in word:
                     if a != b and b != c and c != d and d != e:
                         k += 1
print(k)
print('___________')
print()

# Герасим составляет 7-буквенные коды из букв Г, В, Е, И, Б, Д и А.
# Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две глассные или две согласные.
# Сколько различных кодов может составить Герасим

print('№4')
def isGood(s):
    for i in s:
        if s.count(i) > 1:
            return False
    return True


word1 = 'ЕИА'
word2 = 'ГВБД'
k = 0
for a in word2:
    for b in word1:
        for c in word2:
            for d in word1:
                for e in word2:
                    for f in word1:
                        for g in word2:
                            if isGood(a + b + c + d + e + f + g):
                                k += 1
print(k)
print('___________')
print()

# Сколько существует различных символьных последовательностей длины 6 в алфовите [Б, А, О, Ш, Л и К], которые содержат ровно 2 буквы А

print('№5')
word = 'БАОШЛК'
k = 0
for a in word:
    for b in word:
        for c in word:
            for d in word:
                for e in word:
                    for f in word:
                        s = a + b + c + d + e + f
                        if s.count('А') == 2:
                            k += 1
print(k)
print('___________')
print()

# Сколько существует 3-знач чисел кратных 5, в записи которых используется цифры 0-8, при этом каждая цифра используется не более одного раза

print('№6')
k = 0
for a in range(1, 9):
    for b in range(0, 9):
        for c in [0, 5]:
            if a != b and a != c and b != c:
                k += 1
print(k)
print('___________')
print()

# Иван составляет 4-букыенные коды из букв Д, К, Ь и Е.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить первым и нельзя ставить после глассной.
# Сколько различных кодов может составить Иван?

print('№7')
word = 'ДКЬЕ'
k = 0
for a in 'ДКЕ':
    for b in word:
        for c in word:
            for d in word:
                s = a + b + c + d
                if s.count('ЕЬ') == 0 and s.count('Д') == 1 and s.count('К') == 1 and s.count('Ь') == 1:
                    k += 1
print(k)