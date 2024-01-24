n = int(input())

def func(n):
    if n == 1:
        return 3
    return 2*func(n-1) - 1
print(func(n)**2)