import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))

stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, top[i]])

print(" ". join(map(str, answer)))