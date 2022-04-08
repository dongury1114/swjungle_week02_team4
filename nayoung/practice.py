# ndb의 강의 보며 워밍업!

# n은 떡 개수
# m은 떡 길이

# 둘째줄은 떡의 개별 높이들 [ ]

# 떡 높이의 총합은 항상 m 이상

# 최소 m만큼의 떡을 집에 가져가기 위해 설정할 수 있는 높이의 최대값 출력

# tip
# + 적절한 높이 찾을 때까지 이진 탐색 수행해 높이 h를 반복 조정
# + 이 높이로 자르면 조건이 만족될지 '조건 만족 여부에 따라 탐색 범위를 좁혀서 해결'
# + 절단기 높이는 0부터 10억까지의 정수 중 하나

# 입력값
# 4 6
# 19 15 10 17

import sys

input=sys.stdin.readline

n,m= list(map(int, input().split()))
height = list(map(int,input().split()))

#지정 안 했었음ㅋㅋ start, end값 지정
s=0
e=max(height) #19

#담을 것도 안 만들어줬고..
result =0

while(s<=e):
    total =0 # 잘린 부분 떡
    mid = (s+e)//2
    #현재의 높이로 떡을 잘랐을 떄에 전체 떡의 양을 계산할 수 있게 함
    for i in height:
        #현재의 떡의 길이가 높이보다 더 클 때만 떡을 얻을 수 있으니까
        if i>mid:
            #잘린 부분의 떡을 total 변수에 담음 / 전체 떡을 잘랐을 때 떡 양을 담음
            total += i-mid
    #떡의 양이 부족한 경우 더 많이 자를 수 있게 왼쪽으로 탐색 -1
    if total < m:
        e = mid-1
    # 충분하다면 덜 자르도록 오른쪽으로 탐색 +1
    else:
        #m 이상의 떡을 얻었으면 그게 최대값이니까 result에 기록
        result=mid
        s=mid+1

print(result)



# def ddeok(height,s,e,m):
#     if s>e:
#         return None

#     mid = (s+e)//2

#     if height[mid] == m:
#         return mid
#     elif height[mid]>m:
#         return ddeok(height,m,s,mid-1)
#     else:
#         return ddeok(height,m,mid+1,e)

# result=ddeok(height,m,0,n-1)

# print(result)
