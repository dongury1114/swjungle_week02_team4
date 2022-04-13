import sys
import heapq

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

heap = []
#최소힙 사용
for i in range(N):
    num = (int(input()))

    heapq.heappush(heap, num)
    print(heap)