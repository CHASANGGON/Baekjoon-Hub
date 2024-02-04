arr = [0]*5
for i in range(5):
    arr[i] = int(input())
# 버블 정렬
for i in range(4,0,-1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(int(sum(arr)/5))
print(arr[2])
