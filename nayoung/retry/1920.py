import sys

input=sys.stdin.readline

n=int(input())
nArr = list(map(int,input().split()))
nArr.sort()
m=int(input())
mArr=list(map(int, input().split()))

def search(t,s,e):
    while s<=e:
        mid = (s+e)//2

        if nArr[mid] == t:
            return True
        elif nArr[mid]>t:
            e= mid-1
        else:
            s = mid+1
    return None

for i in range(m):
    if search(mArr[i],0,n-1): #ㅋㅋ 이거 for문 아님^^..
        print(1)
    else:
        print(0)