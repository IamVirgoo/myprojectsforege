with open("D:/Решение 24-го/24data/k7data/k7b-2.txt", 'r') as f:
    s = f.readline()

word = 'DBAC'
while word in s:
    if word[-1] == 'D':
        word += 'B'
    elif word[-1] == 'B':
        word += 'A'
    elif word[-1] == 'A':
        word += 'C'
    elif word[-1] == 'C':
        word += 'D'
print(len(word) - 1)
