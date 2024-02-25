import sys
input = sys.stdin.readline

dwarf = [0]*9
for i in range(9):
    dwarf[i] = int(input())

# 2명을 제외시키면 됨
# 9명의 합을 구한 뒤
# 2명을 빼보면 됨
total = sum(dwarf)
i = 0
while i < 8:
    j = i + 1
    while j < 9:
        if total - dwarf[i] - dwarf[j] == 100:
            dwarf[i], dwarf[j] = 0, 0
            i = 9
            j = 9
        j += 1
    i += 1

dwarf.sort()

for i in range(2,9):
    print(dwarf[i])