import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
def pow(a, b):
    if b == 1: # 지수가 1이면 자기자신 리턴
        return a%c
    # 지수의 절반에 해당하는 값을 미리 구해둔다.
    temp = pow(a, b//2)

    # 만약 지수가 홀수면 한 번 더 곱해줘야 한다.
    if (b%2 == 1):
        return (temp*temp%c)*a%c
    # 지수가 짝수면 절반끼리 곱해서 리턴
    return temp*temp%c

print(pow(a, b))

# 아래 코드는 분할정복이긴 해도 시간초과
# 어쨌든 곱하는 횟수는 같아서 결국 b번 곱하는 시간이 든다.
# 그래도 접근 방법은 점점 감을 잡는 것 같다!
# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())
# result = 1
# def mul(a, b):
#     global result
#     if b>2:
#         left = mul(a, b//2)
#         right = mul(a, b-b//2)
#         if left and right:
#             result = left*right
#         return
#     else:
#         result*=a**b

# mul(a, b)
# print(result%c)