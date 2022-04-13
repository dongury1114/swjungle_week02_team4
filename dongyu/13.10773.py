import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

K = int(input())

num = []
for i in range(K):
    num.append(int(input()))

for i in num:
    if i == 0:
        num.pop(num.index(i)-1)
        num.pop(num.index(i))

print(sum(num))