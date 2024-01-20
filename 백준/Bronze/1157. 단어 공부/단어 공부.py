word = input().lower()
word_process = list(set(word))

word_count = []
for w in word_process:
    word_count.append(word.count(w))

if word_count.count(max(word_count)) >= 2:
    print('?')
else:
    print(word_process[word_count.index(max(word_count))].upper())