n, m = map(int, input().split())

arr = [ i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    new_arr = arr[i-1:j]
    for new_a in new_arr[::-1]:
        arr[i-1] = new_a
        i += 1

for a in arr:
    print(a, end = ' ')

