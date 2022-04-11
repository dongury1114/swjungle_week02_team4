import sys, heapq

input=sys.stdin.readline

n=int(input())

h=[] # storage

for i in range(n):
    x=int(input())

    if x == 0:
        if len(h) == 0: #만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
            print(0)
        else: #x가 '0'이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
            print(heapq.heappop(h))
    else: #만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산
        heapq.heappush(h,x)