# Ходы: +1, *2
# Победа в случае >= 50
# Изначально (5, S)

def countStep(x, y):
    # Если то, куда мы пошли победное, то возвращаем 0
    if x + y >= 50:
        return 0
    # Иначе берём значение из ячейки
    else:
        return a[x][y]

# Обьявили начальные значения

# Значение для выигрыша
win = 50
# Начальное значение в первой куче
s1 = 5
# Создали двумерный массив из нулей
a = []
for i in range(win):
    a.append([0] * win)
# Пробешаем по двумерному массиву с конца
for i in range(win - 1, -1, -1):
    for j in range(win - 1, -1, -1):
        # Если произошла победа, то мы обьявляем, что елемент равен нулю
        if i + j >= win:
            a[i][j] = 0
        # Если победа не произошла, то мы смотрим куда можно походить (используя функцию)
        else:
            s = [countStep(i + 1, j), countStep(i, j + 1), countStep(i * 2, j), countStep(i, j * 2)]
            # Ищем минимальное чётное, максимальное нечётное
            minEven = 1000
            maxOdd = 0
            for el in s:
                if el % 2 == 0 and el < minEven:
                    minEven = el
                if el % 2 != 0 and el > maxOdd:
                    maxOdd = el
            if minEven != 1000:
                a[i][j] = minEven + 1
            else:
                a[i][j] = maxOdd + 1

# Петя выиграл с первого хода:
for j in range(1, win):
    if a[s1][j] == 1:
        print(j, end=' ')
print() # Ваня выиграл с первого хода:
for j in range(1, win):
    if a[s1][j] == 2:
        print(j, end=' ')
print() # Петя выиграет со второго хода
for j in range(1, win):
    if a[s1][j] == 3:
        print(j, end=' ')
print() # Ваня выиграет со второго хода
for j in range(1, win):
    if a[s1][j] == 4:
        print(j, end=' ')
print() # Неудачный ход Пети
for j in range(1, win):
    s = [countStep(s1 + 1, j), countStep(s1, j + 1), countStep(s1 * 2, j), countStep(s1, j * 2)]
    if 1 in s:
        print(j, end=' ')