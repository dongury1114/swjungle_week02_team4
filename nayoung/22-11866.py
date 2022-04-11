# N명의 사람이 원을 이루면서 앉아 [7명]
# K번째 사람을 제거 [3번째]
# n명의 사람이 모두 제거될 때까지 계속
# 원에서 사람들이 제거되는 순서 (n,k) == 요세푸스 순열

from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().split())

q = deque([])

for i in range(1,n+1): 
    q.append(i) #q에 1234567 담김
print('<',end='') # 앞 < 생성

#입력받은 k번째까지 요소를 없애고 요소들을 뒤에 추가 // 요소가 없어질때까지 반복
while q:
    for i in range(k-1): #0-1까지
        q.append(q[0]) #q[0] 뒤에 추가하고
        q.popleft() #앞에 요소 빼주고

    print(q.popleft(),end='') # 앞에 요소 pop 해주면서 출력 [리스트에서 삭제]

    if q:
        print(',',end=' ')

print('>')