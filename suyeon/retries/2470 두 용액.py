import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort() # 정렬해야 투 포인터로 적절히 합 찾을 수 있음

left, right = 0, n-1
min_result = float('inf')
answer = []
while left<right:
    a_left = A[left]
    a_right = A[right]
    
    SUM = a_left + a_right
    if abs(SUM) < abs(min_result):
        min_result = SUM
        answer = [a_left, a_right]
        
    if SUM < 0: # 두 용액의 합이 0보다 작으면 left를 늘려 0에 더 가깝게
        left += 1
    else: # 두 용액의 합이 0보다 크면 right를 줄여 0에 더 가깝게
        right -= 1

print(f'{answer[0]} {answer[1]}')