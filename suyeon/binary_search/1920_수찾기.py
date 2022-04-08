# 1920
# 11:37 -> 11:49
import sys

def BS(A, s, e, x):
    if s>e:
        return 0
    mid = (s+e)//2
    if A[mid] == x:
        return 1
    elif A[mid] > x:
        return BS(A, s, mid-1, x)
    else:
        return BS(A, mid+1, e, x)

N = int(sys.stdin.readline().strip()) 
A = list(map(int, input().split()))
A.sort()

M = int(sys.stdin.readline().strip())
numbers = list(map(int, input().split()))

for i in range(M):
    print(BS(A, 0, N-1, numbers[i]))


"""
5
4 1 5 2 3
5
1 3 7 9 5
"""