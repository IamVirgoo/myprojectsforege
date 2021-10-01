word = 'ЕДКОМ'
k = 0
for a in 'ДКМ':
    for b in word:
        for c in word:
            for d in word:
                k += 1
print(k)