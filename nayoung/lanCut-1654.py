import sys
input = sys.stdin.readline

k,n = map(int,input().split())
# n = int(input())


def func(x): # 매 문제마다 조건에 맞게 구현. 찾고자 하는 index를 찾는 function이다.
    count = 0
    for i in range(1, k+1):
        count += min(x//i, k)
    return count


def binary():
    left, right = 1,k-1 #입력값의 최소, 최댓값 (문제에 있음)
    while left < right:
        mid = left + (right-left) // 2
        if func(mid) < n: # 부등호를 <, >, <=, >= 중에 적절히 골라야 함. 방법은 밑에!
            left = mid + 1
        else:
            right = mid
    return left

print(binary())