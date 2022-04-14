# 최소힙과 비슷한 문제고, 최대힙으로 출력할 줄만 알면 되는 것
# 최대힙으로 출력하기 위해선 '-'를 쓰면 됩니다~

import heapq,sys

input = sys.stdin.readline

n=int(input())
h=[]

for i in range(n):
    x= int(input())

    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h,-x)