n = int(input())
x_lst = []
y_lst = []
for _ in range(n):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
if n == 1:
    print(0)
else:
    x_lst.sort()
    w = x_lst[n-1] - x_lst[0]
    y_lst.sort()
    h = y_lst[n-1] - y_lst[0]
    if w == 0 or h == 0:
        print(0)
    else:
        print(w*h)  