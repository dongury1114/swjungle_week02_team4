import sys
input = sys.stdin.readline
n = int(input())
white, blue = 0, 0
matrix = [list(map(int, input().split())) for _ in range(n)]

def cut(x, y, n):
    global white, blue
    check = matrix[x][y] # 기준이 되는 처음 색상
    # 0,0 을 시작으로, n사이즈를 검사한다면 0~n-1까지 돈다.
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:       # 하나라도 다른 색이면 쪼갬
                cut(x, y, n//2)             # 1사분면
                cut(x, y+n//2, n//2)        # 2사분면
                cut(x+n//2, y, n//2)        # 3사분면
                cut(x+n//2, y+n//2, n//2)   # 4사분면
                return
    
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

cut(0, 0, n)
print(white)
print(blue)