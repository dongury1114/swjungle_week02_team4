# 왼쪽 힙은 최대힙으로 정렬, 오른쪽 힙은 최소 힙으로 정렬
# 왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.
# left가 최대힙인 이유는 들어간 수가 중간값보다 작은 수인데,
# 그 수중 가장 큰 값이 중간값이 되어야 하기 때문에
# 즉, left의 첫 원소가 중간값


import sys, heapq

input=sys.stdin.readline

n=int(input())

leftH=[]
rightH=[]

for i in range(n):
    x= int(input())

    if len(leftH) == len(rightH):
        heapq.heappush(leftH,-x)
    else:
        heapq.heappush(rightH,x)
    
    if rightH and -leftH[0]>rightH[0]: #rightH가 빈 값으로 시작하니까, 이게 비어있지 않아야 참이라는 걸 짜준것
        leftValue = heapq.heappop(leftH)
        rightValue = heapq.heappop(rightH)

        # rightH에 중간값보다 큰 원소가 들어가게 되니 leftH에 첫 원소와 rightH의 첫 원소를 교체해
        # 균형을 유지할 수 있도록 함
        heapq.heappush(leftH,-rightValue)
        heapq.heappush(rightH,-leftValue)

    print(-leftH[0]) #전환