# 상근이는 절단기에 높이 H를 지정
# H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것
# 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
# 첫째 줄에 나무의 수 N  /// 집으로 가져가려고 하는 나무의 길이 M
# 둘째 줄에는 나무의 높이

# 이거 python3으로 돌리면 시간초과 나고, pypy3로 돌리면 돌아가~

import sys

input=sys.stdin.readline

n,m = map(int,input().split())
h=list(map(int,input().split()))

s = 0
e = max(h)

result = 0

while (s<=e):
    cut = 0
    mid = (s+e)//2
    for i in h:
        if i>mid:
            cut += i-mid
    if cut<m:
        e=mid-1
    else:
        result=mid
        s=mid+1

print(result)