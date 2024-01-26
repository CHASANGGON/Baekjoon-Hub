a = []
for _ in range(3):
    a.append(int(input()))
if sum(a) == 180:
    set_a = set(a)
    if len(set_a) == 1:
        print('Equilateral')
    elif len(set_a) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')