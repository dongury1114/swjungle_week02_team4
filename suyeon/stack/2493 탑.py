import sys
input = sys.stdin.readline

def main():
    n = int(input())
    towers = list(map(int, input().split()))
    stack, answer = [], []
    for i in range(n):
        while stack:
            if stack[-1][1] > towers[i]: # 송신할 탑이 있음
                answer.append(stack[-1][0]+1)
                break
            else:
                stack.pop() # 오른 쪽에 더 큰 탑이 있으면 의미 없으므로 pop
        if not stack:
            answer.append(0) # 송신할 탑이 없다는 의미
        stack.append([i, towers[i]])
    print(" ".join(map(str, answer)))
    
main()

# 아래 코드는 시간 초과
# def main():
#     n = int(input())
#     s = []
#     temp = list(map(int, input().split()))

#     for i in range(n):
#         s.append(temp[i])
#         if i == n-1:
#             END = ""
#         else:
#             END = " "
#         if i == 0:
#             print(0, end=END)
#         else:
#             j = len(s)-1
#             while j >= 1:
#                 if s[j-1]>=s[-1]:
#                     print(j, end=END)
#                     break
#                 else:
#                     if j==1:
#                         j-=1g 
#                         print(0, end=END)
#                         break
#                     else:
#                         j-=1
#                         continue

# main()