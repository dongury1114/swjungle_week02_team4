import sys, heapq
input = sys.stdin.readline
n = int(input())
commuting = []
for _ in range(n):
    home, office = map(int, input().split())
    commuting.append([min(home, office), max(home, office)])
d = int(input())

# 끝 점 기준 sorting
commuting.sort(key=lambda x:x[1]) 

cnt = 0
max_cnt = 0
h = []
for i in range(n):
    end = commuting[i][1]
    if commuting[i][1] - commuting[i][0] <= d:
        heapq.heappush(h, commuting[i][0])
    while len(h)>0:
        if end-h[0] > d: # 끝 점이 갱신됐을 때 맨 앞 home이 d안에 포함되지 않는다면
            heapq.heappop(h)
        else: # 포함된다면 확인 끝
            break
    max_cnt = max(len(h), max_cnt)

print(max_cnt)

# # 아래 코드는 맨 앞 home 말고도 계속 start home을 바꿔준 뒤, L의 가장 최댓값을 구해야 함
# # 그런데 그러면 이중 for loop을 사용해야 해서 시간 초과가 예상됨. 
# import sys
# input = sys.stdin.readline

# # home, office 좌표 받기
# n = int(input())
# commuting = []
# for _ in range(n):
#     home, office = map(int, input().split())
#     commuting.append([min(home, office), max(home, office)])

# d = int(input())

# # sorting해서 최대 수 찾기
# # [0] 기준 sort
# commuting.sort(key=lambda x:x[0])
# # [1] 기준 sort
# commuting.sort(key=lambda x:x[1])

# cnt=0
# for i in range(n):
#     if (abs(commuting[i][1] - commuting[0][0]) <= d) and (commuting[i][0] >= commuting[0][0]):
#         cnt += 1
# print(cnt)