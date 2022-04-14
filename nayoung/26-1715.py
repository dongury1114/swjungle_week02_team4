import sys, heapq

input=sys.stdin.readline

n=int(input())
card=[]

for i in range(n):
    heapq.heappush(card,int(input())) #10,20,40 넣어줌

if len(card) == 1:
    print(0) #카드가 1개일 경우 비교를 못 하니까
else:
    R=0 #결과 담을 곳
    while len(card) > 1:
        min1 = heapq.heappop(card) #힙은 기본적으로 최소힙 == 제일 작은 덱 뽑히고 삭제
        min2 = heapq.heappop(card) #젤 작은 덱(min1로 뽑힘1) 다음의 작은 덱 뽑히고 삭제 [40]만 남
        R += min1+min2 # result값에 +30을 해줍니다~
        heapq.heappush(card,min1+min2) # card에 30을 넣어줌 한바퀴 돌았을때 [30,40] 남음

    print(R)