import sys
while 1:
    a = list(map(int,sys.stdin.readline().split()))
    a.sort()
    set_a = set(a)
    len_a = len(set_a)
    if set_a == {0}:
        break
    elif a[2] >= a[0] + a[1]:
        print('Invalid')
    elif len_a == 3:
        print('Scalene')
    elif len_a == 2:    
        print('Isosceles')
    else:
        print('Equilateral')