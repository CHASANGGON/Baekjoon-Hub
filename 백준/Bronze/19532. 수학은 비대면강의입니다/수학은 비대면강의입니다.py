import sys
abcdef = list(map(int,sys.stdin.readline().split()))
y_abcdef = abcdef[:]

mlt_y_1,mlt_x_1,mlt_y_2,mlt_x_2 = abcdef[0],abcdef[1],abcdef[3],abcdef[4]

# y소거해서, x구하기
for i in range(3):
    abcdef[i] *= mlt_x_2
    abcdef[i+3] *= mlt_x_1

# x소거해서, y구하기
for i in range(3):
    y_abcdef[i] *= mlt_y_2
    y_abcdef[i+3] *= mlt_y_1

x = (abcdef[2]-abcdef[5])//(abcdef[0]-abcdef[3])
y = (y_abcdef[2]-y_abcdef[5])//(y_abcdef[1]-y_abcdef[4])
print(x,y)