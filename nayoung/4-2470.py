# 산성 용액은 양의 정수
# 알카리성 용액은 음의 정수
# 둘의 혼합 용액의 특성값은 둘의 합으로 정의
# Q. 두 용액을 혼합해 특성값이 0에 가까운 용액을 만드려고 함
# 첫째줄은 전체 용액의 수 n
# 둘째줄은 배열
# 정렬해야함!! 오름차순으로 출력
# 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는
# 그 중 아무것이나 하나를 출력

# 이분탐색이라고 무조건 mid(중간값)를 만들어야하는 건 아니다.

import sys

input=sys.stdin.readline

n= int(input())
nArray=sorted(list(map(int, input().split()))) #[-99, -2, -1, 4, 98] 오름차순 정렬

s=0
e=n-1
mini = sys.maxsize #최소값

while s<e: #두 값을 모두 이용해야하니까 시작<끝
    tmp = nArray[s]+nArray[e] # 얘네를 while문 밖에서 사용해서 값이 고정되는 바람에 위치가 움직이질 않았음!!!!!
    zero = abs(tmp) # 25줄과 같다
    if zero<mini:
        mini = zero
        result = nArray[s],nArray[e]

    if tmp == 0:
        result = nArray[s],nArray[e]
        break
    if tmp>0: #양수면 더 작은값으로
        e-=1
    else: #음수면 더 큰 값으로
        s+=1

for i in result:
    print(i, end=' ')