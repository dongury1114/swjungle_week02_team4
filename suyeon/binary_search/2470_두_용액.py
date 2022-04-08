# 맨 밑 코드는 시간 초과
# 이 코드는 이중 for문 보다는 반복을 줄여서
# 최소한만 돌도록 left, right 투 포인터를 활용함

import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()

# 이중 포인터 설정
left = 0
right = n-1

# 기준값 & 정답 넣을 리스트
closest = float('inf')

# 투 포인터 진행
while left<right:
    a_left = A[left]
    a_right = A[right]

    SUM = a_left+a_right
    if abs(SUM) < abs(closest):
        closest = abs(SUM)
        answer = [a_left, a_right]

    # 두 용액의 합이 0보다 작으면 왼쪽 값을 늘려 0의 값과 가깝게
    if SUM < 0:
        left += 1
    else: # 반대는 오른쪽 값을 줄여감
        right -= 1

print(f'{answer[0]} {answer[1]}')



# import sys

# n = int(sys.stdin.readline().strip())
# A = list(map(int, sys.stdin.readline().strip().split()))

# closest = 10**9

# for i in range(n):
#     for j in range(n-1, 0, -1):
#         temp = A[i] + A[j]
#         if abs(closest) > abs(temp):
#             closest = temp
#             answer = []
#             answer += [A[i], A[j]]

# print(answer)


