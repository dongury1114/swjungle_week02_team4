# sol.01
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

A, B, C = map(int, input().split())

print(pow(A, B, C))

# sol.02
pow
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

A, B, C = map(int, input().split())

def div(a, b):
    if b == 1:
        return a % C

    tmp = div(a, b // 2)
    if b % 2 == 0:
        return (tmp * tmp) % C
    else:
        return (tmp * tmp * a) % C

print(div(A, B))