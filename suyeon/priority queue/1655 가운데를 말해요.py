import sys, heapq

input = sys.stdin.readline

n = int(input())
h = []
temp = []
for i in range(n):
    heapq.heappush(h, int(input()))
    if i <= 1:
        print(min(h))
    else:
        if len(h)%2 == 0: # 짝수개면
            cnt = len(h)//2-1
        else:
            cnt = len(h)//2
        for j in range(cnt):
            heapq.heappush(temp, heapq.heappop(h))
        print(h[0])
        if i < n-1:
            for j in range(cnt):
                heapq.heappush(h, heapq.heappop(temp))
