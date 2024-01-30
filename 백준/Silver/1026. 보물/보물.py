import sys

n = int(sys.stdin.readline()) # 1~50

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
A_l = [0]*101 # 0~100
B_l = [0]*101

for a in A:
    A_l[a] += 1
for b in B:
    B_l[b] += 1

for i in range(100):
    A_l[i+1] += A_l[i]
    B_l[i+1] += B_l[i]



sorted_A = [0]*n
sorted_B = [0]*n

for i in range(n-1,-1,-1):
    sorted_A[A_l[A[i]]-1] = A[i]
    A_l[A[i]] -= 1
    sorted_B[B_l[B[i]]-1] = B[i]
    B_l[B[i]] -= 1
sum = 0
for i in range(n):
    sum += sorted_A[i]*sorted_B[n-1-i]
print(sum)