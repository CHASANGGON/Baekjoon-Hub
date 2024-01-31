n = int(input())

words = [input() for i in range(n)]

words = list(set(words)) # 중복 제거
words.sort()
words.sort(key=len)

for i in words:
    print(i)