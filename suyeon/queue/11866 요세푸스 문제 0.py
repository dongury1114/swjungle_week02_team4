import sys
from queue import Queue

n, k = map(int, sys.stdin.readline().strip().split())

def Josephus(n, k):
    answer = []
    Q = Queue()
    for v in range(1, n+1):
        Q.put(v)
    while Q.qsize() >= 1:
        for i in range(1, k):
            Q.put(Q.get()) # 핵심 idea 
        answer.append(Q.get()) # k번째 수
    return answer 

answer = Josephus(n, k)
print("<", end='')
for i in range(n):
    if i < n-1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end=">")