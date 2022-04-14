N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    # i >= 1일 때,
    # 지울 수 있는 k의 횟수가 남아있고
    # 지울 수 있는 스택이 남아 있고
    # 스택의 맨 끝 수가 이제 넣을 수 보다 작으면
    # 가진 수를 버리고 새로운 큰 수를 넣어준다.
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    # i == 0일 때, 우선 스택에 넣어준다.
    stack.append(num[i])

print(''.join(stack[:N-K]))