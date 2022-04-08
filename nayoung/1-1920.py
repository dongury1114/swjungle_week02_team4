# n개 정수만큼 배열 입력받아야하고
# 다음줄엔 n개 만큼의 배열
# 다음줄엔 m개의 정수
# 그 다음엔 m개의 array
# 그 안에 x라는 정수가 존재하는지 알아내기 == 출력:존재하면 1 / 안 하면 0
# 그니까 narray에 marray가 존재하는지를!! 1 3 7 9 5 중 1 3 5가 존재하니까 1 1 0 0 1 표시


import sys

input = sys.stdin.readline

n=int(input())
nArray=list(map(int,input().split()))
nArray.sort() # 이 작업도 안 해줬었는데 배웠잖늬.. 이진탐색은 오름차순에서 동작한닥오...
m = int(input())
mArray = list(map(int,input().split()))

def search(target,start,end):
    while start<=end:
        mid = (start+end)//2

        if nArray[mid] == target: #찾는값이라면
            return True #gogo
        elif nArray[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for i in range(m):
    if search(mArray[i],0,n-1):
        print(1)
    else:
        print(0)

# 내가 하려 했던 것은 선형탐색이다. 이분탐색을 안 쓴 거니까 엎어버림
# result =[]
# for i in range(n): #for문 수정
#     for j in range(m):
#         if nArray[i] == mArray[j]:
#             result.append('1')
#         else:
#             result.append('0')

# print(result)