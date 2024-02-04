num = input()
n = len(num)
arr = []
for nu in num: # 숫자로 변환
    arr.append(int(nu))

for i in range(0,n-1): # 버블 정렬
    for j in range(n-1,i,-1):
        if arr[j-1] < arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
# 문자로 변환
s = ''
for i in range(n):
    s += str(arr[i])
print(''.join(s))