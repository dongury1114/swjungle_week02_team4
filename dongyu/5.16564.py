import sys

sys.stdin = open("input.txt")

N, K = map(int,input().split())
level = []
for i in range(N):
    level.append(int(input()))

level.sort()
T = 0
start = min(level)
end = max(level) + K

def Team(array, K):
    T = 0
    for i in level:
        if i >= K:
            break
        T += K - i
    return T

while start <= end:
    mid = (start + end )//2
    if Team(level, mid) <= K:
        T = mid
        start = mid + 1
    else:
        end = mid -1

print(T)
# 최대한 min 값이 같도록 K를 분배해서 최대가 되도록
