#sol.02
import sys

sys.stdin = open("input.txt")

n = int(input())
l = list(map(int, input().split()))










# # sol.01 내맘대로 풀어본 억지스러운 풀이 -> 당연히 메모리 초과
# import sys
# import itertools

# sys.stdin = open("input.txt")
# n = int(input())
# l = list(map(int, input().split()))
# tmp = []
# tmp2 = []
# for i in itertools.combinations(l,2):
#     tmp.append(i)
#     tmp2.append(abs(sum(i)))

# a =tmp2.index(min(tmp2))
# list((tmp[a]))
# for i in tmp[a]:
#     print(i ,end=" ")

