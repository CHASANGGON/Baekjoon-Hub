x_lst = []
y_lst = []
for _ in range(3):
    x, y = input().split()
    x_lst.append(x)
    y_lst.append(y)
for x in x_lst:
    if x_lst.count(x) == 1: print(x, end =' ')
for y in y_lst:
    if y_lst.count(y) == 1: print(y)   