number = int(input())
n = 1
room = 1
while number > n:
    n += 6*room
    room += 1

print(room)