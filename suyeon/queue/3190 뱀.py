import collections
import itertools
import sys
from collections import deque

q = deque()

# 보드 크기
n = int(sys.stdin.readline().strip())

# 사과
k = int(sys.stdin.readline().strip())
apples=[]
for i in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    apples.append([x, y])

# 시간 & 방향
l = int(sys.stdin.readline().strip())
times = {}
turn_times = []
for i in range(l):
    time, dir = sys.stdin.readline().strip().split()
    turn_times.append(int(time))
    times[int(time)] = dir
direction = ['right', 'down', 'left', 'up']

count = 0
x, y = 1, 1
now = [x, y]
dir_num = 0
dir = direction[dir_num]
q.append(now)
while True:
    # 방향에 맞게 이동
    if dir == 'right':
        y+=1
    elif dir == 'down':
        x+=1
    elif dir == 'left':
        y-=1
    elif dir == 'up':
        x-=1
    count+=1
    now = [x, y]

    # 일단 머리 늘리고 큐에 넣고 게임오버 체크 먼저 함
    # 게임오버 아니고 사과 없으면 꼬리 자름
    q.append(now)

    # 게임오버 체크
    # 벽에 닿았거나, 자기 몸에 닿았으면 게임오버
    if x<=0 or y<=0 or x>n or y>n:
        print(count)
        break
    elif len(q)>=4:
        if now in collections.deque(itertools.islice(q, 0, len(q)-2)): # 방금 넣은 머리 제외하고 자기 몸에 닿았는지
            print(count)
            break
    
    # 사과 먹거나 꼬리 자르기
    if now not in apples:
        q.popleft()
    else:
        apples.remove(now)


    # 방향 전환
    if count in turn_times:
        if times[count] == 'L':
            if dir_num>0:
                dir_num-=1
            else:
                dir_num=3
        elif times[count] == 'D':
            dir_num+=1     
            dir_num%=4
        dir = direction[dir_num]