import sys
from collections import deque

q = deque()

n = int(sys.stdin.readline().strip())
for i in range(n):
    order = list(sys.stdin.readline().strip().split())
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'empty':
        if len(q)>0:
            print(0)
        else:
            print(1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif order[0] == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
    elif order[0] == 'pop':
        try:
            print(q.popleft())
        except:
            print(-1)