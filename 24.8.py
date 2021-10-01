with open("D:/Решение 24-го/24data/k7data/k7b-5.txt", 'r') as f:
    s = f.readline()

word = 'CA'
while word in s:
    if word[-1] == 'C':
        word += 'A'
    if word[-1] == 'A':
        word += 'C'
print(len(word) - 1)