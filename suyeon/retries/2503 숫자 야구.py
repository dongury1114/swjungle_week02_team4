# 시험 때 풀지 못한 문제 retry
# 내일 다시 retry

import itertools
import sys

n = int(sys.stdin.readline().strip())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS = list(itertools.permutations(data, 3))

remove_cnt = 0
for _ in range(n):
    number, s, b = input().split()
    remove_cnt = 0
    for i in range(len(NUMBERS)):
        strike = ball = 0
        i -= remove_cnt
        for j in range(3):
            if NUMBERS[i][j] == number[j]:
                strike += 1
            elif number[j] in NUMBERS[i]:
                ball += 1
        
        if int(s) != strike or int(b) != ball:
            NUMBERS.remove(NUMBERS[i])
            remove_cnt += 1

print(len(NUMBERS))