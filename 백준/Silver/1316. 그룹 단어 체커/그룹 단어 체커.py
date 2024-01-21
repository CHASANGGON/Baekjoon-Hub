n = int(input())

total_count = 0
for _ in range(n):
    word = input()
    word_set = list(dict.fromkeys(word))
    before = 0
    count = 1
    for w in word:
        now = word_set.index(w)
        if before > now:
            count = 0
            break
        before = now
    total_count += count

print(total_count)
