string = input()
arr = [-1]*26
i = 0
for s in string:
    if arr[ord(s)-97] == -1:
        arr[ord(s)-97] = i
    i += 1

for i in arr:
    print(i, end =' ')