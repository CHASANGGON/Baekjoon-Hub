import sys

n = int(input())
n_arr = list(map(int,sys.stdin.readline().split()))
input()
m_arr = list(map(int,sys.stdin.readline().split()))
n_count_arr = [0]*20000001

for i in range(n):
    n_count_arr[n_arr[i]+10000000] = 1

for m in m_arr:
    if n_count_arr[m+10000000]:
        print(1,end=' ')
    else:
        print(0,end=' ')