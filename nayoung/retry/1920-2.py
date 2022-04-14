import sys

input=sys.stdin.readline

n=int(input())
nData = sorted(list(map(int, input().split())))
m=int(input())
mData = list(map(int, input().split()))

def search(t,s,e):
    while s<=e:

        mid=(s+e)//2

        if t == nData[mid]:
            return nData[mid]
        elif t>nData[mid]:
            s=mid+1
        else:
            e=mid-1
    return None

for i in range(m):
    if search(mData[i],0,n-1):
        print(1)
    else:
        print(0)