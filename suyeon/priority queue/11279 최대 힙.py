import heapq, sys

n = int(sys.stdin.readline().strip())
A = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            print(-heapq.heappop(A))
        except:
            print(0)
    else:
        heapq.heappush(A, -x)