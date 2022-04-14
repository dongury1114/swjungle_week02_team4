import sys

input=sys.stdin.readline

n,m = map(int,input().split())
h=list(map(int,input().split()))

r=0 #결과 담을 곳
s=0
e=max(h)

while s<=e:
    cut=0 # 자른 거 담을 곳
    mid=(s+e)//2

    for i in h:
        if i>mid:
            cut+=i-mid
    if cut<m:
        e = mid-1
    else:
        r = mid
        s = mid+1

print(r)

# 함수로 풀어봤는데, 안되더라,,,! 그냥 함수로 namu(s,e) 이렇게 담았는데 안되었음 ㅠㅠ