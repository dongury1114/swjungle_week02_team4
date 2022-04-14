# 첫째 줄에는 전체 종이의 한 변의 길이 N
# N은 2, 4, 8, 16, 32, 64, 128 중 하나
# 2^0, 2^1, 2^2 ... 2^n 이렇게  있는 것!
# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서
# 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다
# 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램
# 하얀칸은 0, 파란칸은 1 //// 출력 한 줄 하얀색, 두번째 파란색

# 참고했음 -_-^

import sys

input=sys.stdin.readline

n=int(input()) # 8
arr = [list(map(int, input().split())) for i in range(n)]

result=[]

def paper(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                paper(x,y,n//2)
                paper(x,y+n//2,n//2)
                paper(x+n//2,y,n//2)
                paper(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

paper(0,0,n)
print(result.count(0))
print(result.count(1))