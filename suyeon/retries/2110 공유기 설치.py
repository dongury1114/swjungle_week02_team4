import sys
n, c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 1, houses[-1]-houses[0]
while s<=e:
    gap = (s+e)//2
    now = houses[0]
    cnt = 1
    for i in range(1, n):
        if gap+now <= houses[i]:
            cnt+=1
            now = houses[i]
    
    if cnt >= c: # 공유기 너무 많이 설치. gap 늘림
        s = gap+1
        answer = gap # 왜 그냥 gap 이랑 answer이랑 달라지는건지 궁금
    else:
        e = gap-1

print(answer)