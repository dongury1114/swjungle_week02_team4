# 방향 전환 시 코드 수정 필요함
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

count = 1
x, y = 1, 1
now = [x, y]
dir_num = 0
dir = direction[dir_num]
q.append(now)
while True:
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
    # 방향에 맞게 이동
    count+=1
    if dir == 'right':
        y+=1
    elif dir == 'down':
        x+=1
    elif dir == 'left':
        y-=1
    elif dir == 'up':
        x-=1
    now = [x, y]

    # 게임오버 체크
    # 벽에 닿았거나, 자기 몸에 닿았으면 게임오버
    if (x==0 or y==0 or x==n or y==n) or now in q:
        print(count+1)
        break

    # 방문한 곳 큐에 넣고
    q.append(now)
    # 사과 없으면 꼬리 자름
    if now not in apples:
        q.popleft()

