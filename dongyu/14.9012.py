import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    check = list(input())
    sum = 0

    for j in check:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
