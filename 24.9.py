with open('D:/Решение 24-го/24data/k7data/k7b-6.txt', 'r') as f:
    s = f.readline()

word = 'DAF'
while word in s:
    if word[-1] == 'D':
        word += 'A'
    if word[-1] == 'A':
        word += 'F'
    if word[-1] == 'F':
        word += 'D'
print(len(word) - 1)