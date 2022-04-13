#sol.1
import sys
import heapq

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
heap =[]

for i in range(n):
    m = int(input())
    if m != 0:
        heapq.heappush(heap, -1*m)
    elif m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
#sol.2 같지만 다른 

# import sys
# import heapq

# sys.stdin = open("input.txt")
# input = sys.stdin.readline

# n = int(input())
# heap = []

# for _ in range(n):
#     m = int(input())
#     if m == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print((-1)*heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, (-1)*m)