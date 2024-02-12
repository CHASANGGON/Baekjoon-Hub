import sys
input = sys.stdin.readline

n, k = map(int,input().split())

queue = list(range(1,n+1))

idx = 0
Josephus = []
while queue: 
    idx = (idx+k-1)%len(queue)  # 처음에는 k-1부터 시작해야하고,
                                # 그 다음부터는 pop하면 길이가 줄어드니까 k-1 씩 더해야해
    Josephus.append(str(queue.pop(idx)))
    
print('<', ', '.join(Josephus), '>',sep='')