import sys,heapq

input=sys.stdin.readline

card=[]

n=int(input())

for i in range(n):
    heapq.heappush(card,int(input()))

if len(card) ==1:
    print(0)
else:
    R=0
    while len(card)>1:
        min1=heapq.heappop(card)
        min2=heapq.heappop(card)
        R+=min1+min2
        heapq.heappush(card,min1+min2)

    print(R)

    # 약간 외워서 푼 것 같기도 한데... ㅋ... evande~