# 최대 힙과 최소 힙 모두 사용 ver.
import sys, heapq

input = sys.stdin.readline
n = int(input())
max_h = []
min_h = []

for i in range(n):
    z = int(input())

    if len(max_h) - len(min_h) >= 1: # max_heap의 크기가 min_heap의 크기보다 1 크거나 같게 유지
        # min_heap에 넣을 타이밍
        heapq.heappush(min_h, z)
    else:
        heapq.heappush(max_h, -z)

    # max_heap의 top > min_heap의 top이면 서로 바꿈
    if min_h and (-max_h[0] > min_h[0]):
        max_top = -heapq.heappop(max_h)
        min_top = heapq.heappop(min_h)
        heapq.heappush(min_h, max_top)
        heapq.heappush(max_h, -min_top)
    
    # 그럼 max_heap의 top이 중간값임
    print(-max_h[0])



# 아래 코드는 시간 초과
# import sys, heapq

# input = sys.stdin.readline

# n = int(input())
# h = []
# temp = []
# for i in range(n):
#     heapq.heappush(h, int(input()))
#     if i <= 1:
#         print(min(h))
#     else:
#         if len(h)%2 == 0: # 짝수개면
#             cnt = len(h)//2-1
#         else:
#             cnt = len(h)//2
#         for j in range(cnt):
#             heapq.heappush(temp, heapq.heappop(h))
#         print(h[0])
#         if i < n-1:
#             for j in range(cnt):
#                 heapq.heappush(h, heapq.heappop(temp))
