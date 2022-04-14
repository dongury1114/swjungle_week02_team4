import sys

n,c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 1, houses[-1]-houses[0] # 간격의 최소, 최대값
while s<=e:
    gap = (s+e)//2 # 두 집 사이의 거리
    now = houses[0] # 현재 공유기를 설치한 집
    cnt = 1 # 공유기 개수

    for i in range(1, n):
        if now+gap <= houses[i]:
            cnt += 1
            now = houses[i]
    
    if cnt >= c: # 공유기 너무 많이 설치. gap 넓혀야 함
        s = gap+1
    else: # 공유기 적게 설치. gap 줄여야 함
        e = gap-1

print(e) # 처음 버전 답과 다른 점 : e를 애초에 간격의 최대값으로 설정했으므로, 반복문이 끝난 뒤의 e가 정답임
