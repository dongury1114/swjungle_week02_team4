#sol.01
import heapq
import sys

sys.stdin = open("input.txt")
N = int(input())
card_deck = []
for _ in range(N):
    heapq.heappush(card_deck, int(sys.stdin.readline()))


if len(card_deck) == 1: #1개일 경우 비교하지 않아도 된다
    print(0)
else:
    answer = 0
    while len(card_deck) > 1: #1개일 경우 비교하지 않아도 된다
        temp_1 = heapq.heappop(card_deck) #제일 작은 덱
        temp_2 = heapq.heappop(card_deck) #두번째로 작은 덱
        answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
        heapq.heappush(card_deck, temp_1 + temp_2) #더한 덱을 다시 넣어줌
    
    print(answer)

# sol. 02

import heapq # 우선순위 큐
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
cardList = []
# cardList = list(int(input()) for _ in range(N))

for _ in range (N):
    cardList.append(int(input()))
    
heapq.heapify(cardList)
sum=0


while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    sum += num1 + num2
    # result += Sum
    heapq.heappush(cardList,sum)

print(sum)
