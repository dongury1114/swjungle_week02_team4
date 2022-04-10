import heapq, sys

n = int(sys.stdin.readline().strip())
SUM = 0
h = []
for i in range(n):
    heapq.heappush(h, int(input()))

while len(h)>1:
    s1 = heapq.heappop(h)
    s2 = heapq.heappop(h)
    SUM += s1+s2
    heapq.heappush(h, s1+s2)

print(SUM)