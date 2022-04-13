# 1629 곱셈 문제와 동일한 방식!
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]
                temp[i][k] %= 1000
    return temp
    
def matrix_pow(matrix, b):
    if b == 1: # 지수가 1이면 자기자신 리턴
        return matrix
    half = matrix_pow(matrix, b//2)

    # 만약 지수가 홀수면 한 번 더 곱해줘야 한다.
    if (b%2 == 1):
        temp = matrix_mult(half, half)
        return matrix_mult(matrix, temp)
    
    # 지수가 짝수면 절반끼리 곱해서 리턴
    return matrix_mult(half, half)

def print_matrix(matrix):
    for i in range(n):
        print(" ".join(map(str, matrix[i])))

# 지수가 1일 때는 함수 실행 필요 없음
if b == 1:
    for i in range(n):
        for j in range(n):
            print(matrix[i][j]%1000, end=' ')
        print()
else:
    print_matrix(matrix_pow(matrix, b))