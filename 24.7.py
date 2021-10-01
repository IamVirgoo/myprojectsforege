with open("D:/Решение 24-го/24data/k7data/k7b-4.txt", 'r') as f:
    s = f.readline()


word = 'EBCF'
while word in s:
    if word[-1] == 'E':
        word += 'B'
    if word[-1] == 'B':
        word += 'C'
    if word[-1] == 'C':
        word += 'F'
    if word[-1] == 'F':
        word += 'E'
print(len(word) - 1)