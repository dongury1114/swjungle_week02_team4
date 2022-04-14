# 첫째 줄에 행렬의 크기 N과 B가 주어진다
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력
# A^B의 각 원소를 1,000으로 나눈 나머지를 출력

import sys

input = sys.stdin.readline

n,b = map(int,input().split()) #ok
a = [list(map(int, input().split())) for i in range(n)] #[[1, 2], [3, 4]]

def matrix(a,trix):
    # [[0]*2]*2로 풀면 리스트가 공유되어서 다른 결과가 나옴
    tmp = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += (trix[i][k]*a[k][j]) #잘못 곱하고 있었다니ㅠㅠ
            tmp[i][j]%=1000

    return tmp

def mul(a,b):
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    # 홀수인 경우엔, a를 마지막에 곱해주어야 한다고 한다~
    # aaaaa → (a^2)^2*a
    elif b%2 == 1:
        trix = mul(a,b-1)
        newTrix = matrix(a,trix)
        return newTrix
    # 짝수인 경우엔, 제곱수를 계속해서 곱해야 한다
    # aaaaa → (a^2) = aa → (a^2)^2 = aaaa
    else:
        trix=mul(a,b//2)
        newTrix=matrix(trix,trix)

        return newTrix

result = mul(a,b)
for row in result:
    print(*row)
    # 매개변수 'row'를 가변적인 갯수를 가진 위치 인수로 정의하겠다는 의미
    # 가변 갯수의 위치 인수로 설정했기 때문에 임의의 변수들인 w,e 이런거여도 잘 동작한다고 한다~