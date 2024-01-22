arr = [ list(map(int, input().split())) for _ in range(9) ] 
max_arr = []
for ar in arr:
    max_arr.append(max(ar))

max_value = max(max_arr)
i = max_arr.index(max(max_arr))+1
j = arr[i-1].index(max_value)+1
print(max_value)
print(i, j)