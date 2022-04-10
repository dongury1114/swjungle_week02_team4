import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()

s, e = 0, n-1
min_result = float('inf')
result = []
while s<e:
    SUM = A[s] + A[e]
    
    if abs(SUM) <= abs(min_result):
        min_result = SUM
        result = [A[s], A[e]]

    if SUM <= 0: # 합이 0보다 작으면 시작점 오른쪽으로
        s+=1
    else: # 0보다 크면 끝 점 왼쪽으로
        e-=1

print(f'{result[0]} {result[1]}')