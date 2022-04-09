import sys

n, k = map(int, sys.stdin.readline().strip().split())
Characters = []
for i in range(n):
    Characters.append(int(sys.stdin.readline().strip()))

s, e = 1, max(Characters)
while s<=e:
    level_up = 0
    mid = (s+e)//2
    for character in Characters:
        if character <= mid:
            level_up += mid-character
    
    if level_up <= k:
        s = mid+1
    else:
        e = mid-1
print(e)