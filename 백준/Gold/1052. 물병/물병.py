import sys
input = sys.stdin.readline

nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 
        2048, 4096, 8192, 16384, 32768, 65536, 131072, 
        262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]
n, k = map(int, input().split())
if n <= k:
    print(0)
else:    
    while k != 1 and n != 0:
        before = 1
        for num in nums:
            if n <= num:
                break
            else:
                before = num
        n -= before
        k -= 1
        
    if n:
        for num in nums:
                if n <= num:
                    print(num - n)
                    break
                else:
                    before = num
    else:
        print(0)