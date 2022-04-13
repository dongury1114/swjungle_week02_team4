import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque([])
for i in range(1, n+1):
    que.append(i)

# print(que)

while len(que) != 1:
    que.popleft()
    tmp = que.popleft()
    que.append(tmp)

print(que[0])
