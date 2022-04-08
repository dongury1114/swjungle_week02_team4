# N개의 캐릭터 /// 각 캐릭터의 레벨은 Xi /// 레벨을 최대 총합 K만큼 올릴 수 있다.
# 팀 목표레벨 T =min(Xi) (1 ≤ i ≤ N)라고 정의
# 가능한 최대 팀 목표레벨 T를 출력

# 첫째 줄에는 캐릭터의 개수 N, 올릴 수 있는 레벨 총합 K가
# 각 캐릭터의 레벨이 X1, X2, X3, ... , Xn 으로 주어진다

import sys

input = sys.stdin.readline

n,k = map(int, input().split())
x=[int(input()) for i in range(n)] #여기다가 split 넣고 왜 안 되지 이러고 있었넼ㅋㅋ
x.sort() #[10, 15, 20] 오름차순으로 정렬!

def cnt(x,mid):
    t=0
    for n in x:
        if n>=mid:
            break
        t+=mid-n
    return t

s,e = min(x),max(x)+k
result = 0

while s<=e:
    mid=(s+e)//2
    if cnt(x,mid) <= k:
        result = mid
        s = mid+1
    else:
        e = mid-1
print(result)