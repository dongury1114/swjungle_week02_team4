import sys
from collections import deque

input=sys.stdin.readline

n =int(input())

card= deque([i for i in range(1,n+1)]) # 한꺼번에 받는걸 아직 모르겠어..
# for i in range(1,n+1):
#     card=deque(i)

while card:
    print(card.popleft(),end=' ') #리스트에서 지우고 나중에 꺼낼때 ' '를 포함해 꺼냄
    if card:
        card.append(card.popleft()) #방금 popleft한 수를 꺼내서 붙여줌