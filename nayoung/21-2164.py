from collections import deque
import sys

input=sys.stdin.readline

n=int(input())

card = deque([i for i in range(1,n+1)])

while len(card)>1: #우리가 출력하고자 하는 건 1개니까 1개 이상이면
    card.popleft() #반복적으로 없애!
    keep = card.popleft() #그리고 담아
    card.append(keep) #젤 마지막에 남던 친구까지 없애서 pop해주면 끗

print(card[0]) #첫째줄에 남게 되는 카드 번호를 출력하는 거니까 0번째 써줘야지ㅠㅠ