from collections import deque
import sys
input = sys.stdin.readline

# 제일 위의 카드 1장을 바닥에 내려놓는다.
# 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때
# 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때

# 입력
n = int(input())
skills = list(map(int, input().split()))

# 놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, N
# 왼쪽이 젤 아래 / 오른쪽이 젤 위
cards = list(range(n,0,-1)) # 현재 카드

# 초기 카드 상태를 나타낼 변수
# 왼쪽이 젤 아래 / 오른쪽이 젤 위
origin = deque() 

for skill in skills[::-1]: # 스킬 반전 시키기
    if skill == 1: # 젤 위에서 뽑은 경우
        origin.append(cards.pop()) 
    
    if skill == 2:
        temp = origin.pop()
        origin.append(cards.pop())
        origin.append(temp)

    if skill == 3:
        origin.appendleft(cards.pop())


print(*list(origin)[::-1])