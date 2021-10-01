with open("D:/Решение 24-го/24data/k7data/k7b-2.txt", "r") as f:
    s = f.readline()


word = 'BAFD'
while word in s:
    if word[-1] == 'B':
        word += 'A'
    if word[-1] == 'F':
        word += 'D'
    if word[-1] == 'D':
        word += 'B'
print(len(word) - 1)