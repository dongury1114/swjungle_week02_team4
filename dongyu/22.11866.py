from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int,input().split())

que = []
answer = []
for i in range(1, N+1):
    que.append(i)

popNum= 0

while que:
    popNum = (popNum + (K-1)) % len(que) 
    popElemnet = que.pop(popNum)
    answer.append(str(popElemnet))
print(f"<{', '.join(answer)}>")

#sol.2
import sys
from collections import deque
input = sys.stdin.readline

n, k= map(int,input().split())
que = deque([])
for i in range(1, n+1):
    que.append(i)

answer = []
print("<",end='')
while que:
    for _ in range (k-1):
        que.append(que.popleft())
    print(que.popleft(),end="")
    if que:
        print(", ",end="")
print(">")
