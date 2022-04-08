# 16564
# 나무자르기 문제와 반대
# 나무자르기 문제에서는 길면 자르는거였다면,
# 이 문제는 짧으면 더하는 방향으로!

import sys

N, K = map(int, sys.stdin.readline().strip().split())
X = []
for i in range(N):
    X.append(int(sys.stdin.readline().strip()))


s, e = 1, max(X)
while s<=e:
    m = (s+e)//2
    level_up = 0

    for x in X:
        if x <= m:
            level_up += (m-x)
    
    if level_up <= K:
        s = m + 1
    else:
        e = m - 1

print(e)