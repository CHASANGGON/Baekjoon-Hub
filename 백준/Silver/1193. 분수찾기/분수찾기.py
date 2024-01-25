n = int(input())

line = 1
total = 1
while n > total:
    line += 1
    total += line

if line % 2 == 0: # 위 -> 아래
    y = total - n + 1
    x = line + 1 - y
else:
    x = total - n + 1
    y = line + 1 - x

print(f'{x}/{y}')