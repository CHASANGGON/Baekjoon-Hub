N = int(input())
star = '*'

for _ in range(N):
    print(star.rjust(N))
    star += '*'