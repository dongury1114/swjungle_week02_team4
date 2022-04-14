from collections import Counter
import sys

input=sys.stdin.readline

n=int(input())
nData=sorted(list(map(int,input().split())))
m=int(input())
mdata=list(map(int,input().split()))

def search(t,s,e):
    while s<e:
        mid =(s+e)//2
        
        if nData[mid]<=t:
            s=mid+1
        else:
            e=mid
    return nData[s]

cnt= Counter(nData)
r = []
for i in range(m):
    if mdata[i] in cnt:
        r.append(cnt[mdata[i]])
    else:
        r.append(0)

print(" ".join(map(str, r)))

# 구현법은 수 찾기(1920)과 동일한데, 다만 거기서 몇 개 가지고 있는지를 표시해야하는데,
# 그걸 어떻게 하는 지를 못 찾음 == 구글링으로 찾음!!!!!!!!!!!!!!!!!!!!
# counter 함수를 사용했습니다~
# Counter는 리스트를 값으로 주게 되면 해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환

# 출력에서 문제가 생겨서 append 이용해 출력.... 근데.. 또 실패;; why??