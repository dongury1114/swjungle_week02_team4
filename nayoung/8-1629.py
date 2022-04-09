# (a를 b번 곱한 수)를 c로 나눈 나머지를 구하는 프로그램
# 첫째줄에 a,b,c가 빈 칸을 사이에 두고 순서대로

import sys

input=sys.stdin.readline

a,b,c = map(int, input().split())

# mul = a**b
# mod=mul%c

# print(mod) # 시간초과 납니다^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# b를 분할하여 곱셈을 진행할때마다 c로 나눈 나머지로 만들어 반환
# c로 나눈 나머지므로 계속 나눈 나머지를 곱해도 결과는 동일하대

def divi(a,b):
    if b == 1:
        return a%c
    elif b==2:
        return a*a%c
    else:
        tmp=divi(a,b//2)

        if b%2==0:
            return tmp*tmp%c
        else:
            return tmp*tmp*a%c

result = divi(a,b)
print(result)