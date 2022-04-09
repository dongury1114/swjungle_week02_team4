import sys
# queue로 하면 시간초과
# from queue import Queue

# n = int(sys.stdin.readline().strip())

# q = Queue()
# for i in range(1, n+1):
#     q.put(i)

# while q.qsize()>1:
#     q.get()
#     q.put(q.get())

# sys.stdout.write(str(q.get()))

from collections import deque
n = int(sys.stdin.readline().strip())
q = deque(i for i in range(1, n+1))

while len(q)>1:
    q.popleft()
    q.append(q.popleft())

sys.stdout.write(str(q.pop()))