# 스택으로 푸는 방법 retry 필요
import sys
n = int(sys.stdin.readline().strip())
H = []
for _ in range(n):
    H.append(int(sys.stdin.readline().strip()))

cnt = n
MIN = H[-1]
for i in range(n-2, 0, -1):
    if MIN >= H[i]:
        cnt-=1
    else:
        MIN = H[i]

if MIN >= H[0]:
    cnt-=1

print(cnt)