import sys

sys.stdin = open("input.txt")
# input = sys.stdin.readline


n = int(input())


# for i in range(n):
#     check = list(input())
#     sum = 0
#     for j in check:
#         if j == "(":
#             sum += 1
#         elif j == ")":
#             sum -= 1
#         if sum < 0:
#             print("NO") #이 부분이 이해하기 어려웠다, 괄호를 만들때 ()) -> sum 이 음수가 되는 순간은 이후에도 더 볼 이유 없이 정답이 불가능하기 때문에 NO 출력 후 브레이크
#             break
#     if sum > 0:
#         print("NO")
#     elif sum == 0:
#         print("YES")


for i in range(n):
    check = input()
    sum = 0
    for j in check:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    if sum >0:
        print("NO")
    elif sum == 0:
        print("YES")