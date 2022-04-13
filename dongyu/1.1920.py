# #sol.01 리스트로 수행시 시간초과 -> 집합 자료형
# n = int(input())
# N = set(input().split())
# m = int(input())
# M = input().split()

# for i in M:
#     # 여기서 이진탐색 활용
#     print('1') if i in N else print('0')


 
# #sol.02 -> 참고코드
# from sys import stdin, stdout
# n = stdin.readline()
# N = set(stdin.readline().split())
# m = stdin.readline()
# M = stdin.readline().split()

# for l in M:
#     stdout.write('1\n') if l in N else stdout.write('0\n')

# ------------------------------------------------------------------

# N=int(input())
# nums_1=list(map(int,input().split()))

# M=int(input())
# nums_2=list(map(int,input().split()))

# check=False
# for i in nums_2:
#     check=False
#     for j in nums_1:
#         if i==j:
#             check=True
#             print(1)
#             break
#     if check==False:
#         print(0)

#sol.03 이진탐색

import sys

sys.stdin = open("input.txt")

n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

def binary_search(N, M):
    start = 0
    end = len(N) -1

    while start <= end:
        mid = (start + end)//2
        if M == N[mid]:
            return 1
        elif M > N[mid]:
            start = mid + 1
        elif M < N[mid]:
            end = mid -1
    return 0

for i in range(m):
    print(binary_search(N, M[i]))


#return을 하지 않았음
#mid 괄호