word = input()

sum = 0
for w in word:
    if w in 'ABC':
        sum += 3
    elif w in 'DEF':
        sum += 4
    elif w in 'GHI':
        sum += 5
    elif w in 'JKL':
        sum += 6
    elif w in 'MNO':
        sum += 7
    elif w in 'PQRS':
        sum += 8
    elif w in 'TUV':
        sum += 9
    else:
        sum += 10
print(sum)