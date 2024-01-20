abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

count = [0]*26
word = input()
for w in word:
    a = abc.index(w)
    if a >= 26:
        a -= 26
    count[a] += 1

max = count[0]
max_index = 0
for i in range(26):
    if max < count[i]:
        max = count[i]
        max_index = i

check = 0
for i in range(26):
    if count[i] == max:
        check += 1
if check >= 2:
    print('?')
else:
    print(chr(max_index+65))