# 첫째 줄에 집의 개수 N //// 공유기의 개수 C가 하나 이상의 빈 칸을 사이에 두고 설치
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi가 한 줄에 하나씩
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력

# 풀이를 봤는데 만족하는 거리가 2,3밖에 없고 그 중에서 최대값은 그럼 누구냐?
# => 둘 다 3이라서(=최대값) 그냥 답이 3이다~~!
# https://tmdrl5779.tistory.com/119

import sys

input=sys.stdin.readline

n,c = map(int,input().split())
x=sorted([int(input()) for i in range(n)]) #[1, 2, 4, 8, 9] 입력 받고 정렬 진행

def search(start,end):
    while start<=end:
        mid= (start+end)//2 #4

        cnt = 1
        wifi =min(x)+mid #거리=5 ?

        for i in range(1,n):
            if wifi <= x[i]: #x[3]=8부터
                cnt += 1
                wifi = x[i]+mid #다음 설치칸

        if cnt >= c: #얼마나 설치했는지, 부족하거나 많다면 중단값 조절
            start = mid+1
        else:
            end = mid-1
    return end

print(search(1,max(x)-min(x)))
# start=1인 이유는 하나 이상의 빈 칸을 두고 설치 == 최소값이 1
# end는 max값과 min값의 차이 == 8