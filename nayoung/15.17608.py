# 첫 번째 줄에는 막대기의 개수를 나타내는 정수 N
# N줄 각각에는 막대기의 높이를 나타내는 정수 h
# 오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력

import sys

input = sys.stdin.readline

n=int(input())

stack=[]

for i in range(n):
    stack.append(int(input())) #그냥 바로 해도 되자너~

max=stack[-1] # 이게 오른쪽에서 쳐다볼때 제일 처음 값이니까! 기준이 되는거임.
cnt = 1 #그래서 1개는 무조건 보이니까, 1부터
    
for i in range(n):
    tmp = stack.pop() #하나씩 꺼내서 비교
    if max <tmp:
        cnt+=1
        max=tmp

print(cnt)