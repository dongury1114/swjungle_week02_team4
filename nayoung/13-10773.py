# oh 생각보다 ez하게 풀었어!!!

import sys

input=sys.stdin.readline

k = int(input())

stack = []

for i in range(k):
    arr = int(input())

    if arr == 0:
        stack.pop()
    else:
        stack.append(arr)

print(sum(stack))