n = int(input())

word_front = 1 # B
word_back = 0 # A
if n != 1:
    for _ in range(n-1):
        temp = word_front
        word_front += word_back
        word_back = temp

print(word_back, word_front)