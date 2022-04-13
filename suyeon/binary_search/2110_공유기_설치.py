import sys

n,c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 0, 10**9
while s<e:
    gap = e+(e-s)//2
    now = houses[0]
    cnt = 1

    for i in range(1, n):
        if now+gap <= houses[i]:
            cnt += 1
            now = houses[i]
    
    if cnt >= c: # 공유기 너무 많이 설치. gap 넓혀야 함
        s = gap+1
    else: # 공유기 적게 설치. gap 줄여야 함
        e = gap

print(s-1) # s-1 != gap인 이유는? 코치님한테 물어보기
