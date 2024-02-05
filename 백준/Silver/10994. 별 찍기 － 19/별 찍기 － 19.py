# 별찍기
n = int(input())
lst = []
def make_star(n, lst):
    if n == 1:
        return '*'
    else:
        lst = list(make_star(n-1, lst))

        lst = ['*'+' '*(4*n-5)+'*'] + lst
        lst = ['*'*(4*n-3)] + lst
        for i in range(2,4*n-5):
            lst[i] = '* ' + lst[i] + ' *'
        lst += ['*'+' '*(4*n-5)+'*']
        lst += ['*'*(4*n-3)]
        
        return lst

for star in make_star(n, lst):
    print(star)