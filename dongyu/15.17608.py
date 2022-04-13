import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
stick = []

for _ in range(N):
    stick.append(int(input()))


count = 0
start = 0

for i in range(1, N+1):
    target = stick[-i]
    if target > start:
        count += 1
        start = target
print(count)


# for i in range(0, N):
#     if stick[i] == stick [-1]:
#         count += 0
#     elif stick[i] >= stick[-1]:
#         if stick[i] >= stick[i-1]:
#             count += 1
# print(count)




################################################################################################################################################
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                            나는                                                                                                               #
#                                                                                                                                              #
#                                       바                                                                                                     #
#                                                                                                                                              #
#                                              보                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                      ㄷr                                                                                      #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
#                                                                                                                                              #
################################################################################################################################################



