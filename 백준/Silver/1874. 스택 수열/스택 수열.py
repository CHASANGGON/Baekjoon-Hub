nn = int(input())

lst = []
stack = []
for _ in range(nn):
    lst.append(int(input()))

n = 1
i = 0
my_lst = []
st = ''
while i < nn:
    if n > lst[i]:
        my_lst.append(stack.pop())
        st += '-'
        i += 1
    else:
        stack.append(n)
        st += '+'
        n += 1
if lst == my_lst:
    for s in st:
        print(s)
else:
    print('NO')