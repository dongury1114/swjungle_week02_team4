# 입력은 T개의 테스트 데이터
# 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T
# 괄호 검사는 스택의 대표 예제!

import sys

input=sys.stdin.readline

t = int(input())
stack = []

for i in range(t):
    arr = list(input()) #이거 []로 담으니까 오류난다..

    total=0

    for i in arr:
        if i == '(':
            total+=1
        elif i == ')':
            total-=1 #최종적으로 total이 0이 되면 끝남
        if total<0:
            print('NO')
            break #이거 안 쓰면 출력초과 나옴ㅋㅋ

    if total>0: #total이 0보다 크다면 문자열에 (가 하나 더 있는거라 no!
        print('NO')
    elif total == 0:
        print('YES') # 0이라면 () 이렇게 맞물리는 거니까!