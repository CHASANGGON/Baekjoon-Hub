n = int(input())
standing = list(map(int, input().split()))
waiting_room = []
result = 'Nice'
order = 1

while standing:
    if standing[0] == order:
        standing.pop(0)
        order += 1
    else:
        waiting_room.append(standing.pop(0))
 
    while waiting_room:
        if waiting_room[-1] == order:
            waiting_room.pop()
            order += 1
        else:
            break
 
if waiting_room: 
    result = 'Sad'

print(result)