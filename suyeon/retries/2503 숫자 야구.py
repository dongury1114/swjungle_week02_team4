# 시험 때 풀지 못한 문제 retry
# 

import itertools
import sys

n = int(sys.stdin.readline().strip())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS = list(itertools.permutations(data, 3))
print(NUMBERS)

for NUM in NUMBERS:
    number, s, b = input().split()
    strike = ball = 0
    for i in range(3):
        if NUM[i] == number[i]:
            strike += 1
        elif NUM[i] in number:
            ball += 1
    
    if int(s) != strike or int(b) != ball:
        NUMBERS.remove(NUM)

print(len(NUMBERS))