n = int(input())

score = list(map(int, input().split()))
max = score[0]
for i in range(1,n):
    if score[i] > max:
        max = score[i]

sum = 0
for i in range(n):
    sum += (score[i]/max)*100

print(sum/n)
