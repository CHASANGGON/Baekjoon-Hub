n = int(input())

for _ in range(n):
    lst = list(input())
    y_or_n = 'YES'
    l_count, r_count = 0, 0
    for l in lst:
        if l == '(':
            l_count +=1
        else:
            r_count +=1
            if r_count > l_count:
                y_or_n = 'NO'
                break
    if lst.count('(') != lst.count(')'): 
        y_or_n = 'NO'
    print(y_or_n) 