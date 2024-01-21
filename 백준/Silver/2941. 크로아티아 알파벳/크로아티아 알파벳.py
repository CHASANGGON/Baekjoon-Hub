cro = 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
word = input()
for c in cro:
    if word.count(c) > 0:
        word = word.replace(c,'a')
print(len(word))