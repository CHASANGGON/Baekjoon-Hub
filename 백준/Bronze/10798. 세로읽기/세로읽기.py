arr = [ input() for _ in range(5) ]

len_arr = []
for ar in arr:
    len_arr.append(len(ar))
for i in range(max(len_arr)):
    if i < len(arr[0]) : print(arr[0][i], end='')
    if i < len(arr[1]) : print(arr[1][i], end='')
    if i < len(arr[2]) : print(arr[2][i], end='')
    if i < len(arr[3]) : print(arr[3][i], end='')
    if i < len(arr[4]) : print(arr[4][i], end='')