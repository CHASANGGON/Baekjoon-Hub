import sys
input = sys.stdin.readline

word = input().rstrip()
length = len(word)

suffix = ['']*length
for i in range(length):
    suffix[i] = word[i:]
suffix.sort()

for s in suffix:
    print(s)