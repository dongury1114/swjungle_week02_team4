"""
i행의 숫자들은 i*1, i*2, i*3, ..., i*N으로 구성되어 있다.
i행의 숫자들 중 m보다 작거나 같은 숫자의 개수는 (i*j <= m)를 만족하는 j의 개수이고
이는 i*1, i*2, ..., i*j이므로, m/i와 같은 값이 된다.
"""

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    k = int(input())

    s, e = 1, k # k번째 수는 k보다 클 수 없다.
    while s<e: # s == e일 때는 굳이 고려하지 않는다.
        temp = (s+e)//2 # 임의의 수를 중간 값으로 정해줌.
        cnt = 0
        for i in range(1, n+1):
            # temp보다 작은 수의 개수를 더해주는데, 
            # 이 때 배열의 최대 크기가 한정적이어서 
            # n보다 큰 수가 들어갈 수 없도록 
            # 최대 n개 까지만 들어갈 수 있게 설정해준다.
            cnt += min(temp//i, n) 

        if cnt < k: # temp보다 작은 수의 개수가 k개 보다 더 적다면 k번째 수가 아님.
            s = temp + 1 # 임의의 수를 키워주기 위해 시작 값을 오른쪽으로 당겨서 큰 수로 배정.
        else: 
			# temp == k일 때는 조건을 만족하므로, 
			# e를 왼쪽으로 당겨서 s==e를 만들어주고 while문이 돌지 않게 함.

			# temp보다 작은 수의 개수가 k개 보다 많다면 k번째 수가 아님.
            e = temp # 임의의 수를 작게 해주기 위해 끝 값을 왼쪽으로 당겨서 큰 수로 배정
    print(s)
main()