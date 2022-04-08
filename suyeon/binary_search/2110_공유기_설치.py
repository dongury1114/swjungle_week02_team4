# 2110 
"""
두 집 사이의 거리(gap)를 가지고 이분탐색
적절한 gap일 때 '공유기 설치 cnt 값 == 주어진 공유기의 개수' 조건이 맞게 됨.
"""

import sys

n, c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 1, houses[-1]-houses[0] # 간격의 최소, 최대값
answer = []
while s<=e:
    gap = (s+e)//2 # 두 집 사이의 거리
    cnt = 1
    now = houses[0]

    for house in houses:
        if now+gap <= house: # gap 만큼 벌어진 다음 집에 공유기 설치
            cnt+=1
            now = house
    
    if cnt >= c: # 주어진 공유기 개수보다 많이 셌으면 더 간격 넓혀도 됨
        s = gap+1
        answer.append(gap)
    else: # 간격 좁히기
        e = gap-1

print(max(answer))