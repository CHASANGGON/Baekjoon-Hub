n = int(input())
rect = [ [0]*100 for _ in range(100) ]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            rect[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if rect[i][j] == 1:
            count += 1
print(count)