# 2805
# retry 필요
# 이 경우에는 나무의 벌목 높이를 1~나무 높이들 중 최댓값 중에서 찾아가기 때문에,
# 나무 높이 list를 sort할 필요 없다.

# sort 하면 python에서도 돌아가지만 느림
# 제출은 pypy3로!

import sys
n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

s, e = 1, max(trees)

while s<=e:
    mid = (s+e)//2
    get_tree = 0

    for tree in trees:
        if tree >= mid:
            get_tree += (tree - mid) # 벌목된 만큼 더해줌
    
    # 적절한 벌목 높이를 정해줌
    if get_tree >= m: # 위에서 구한 벌목양이 얻어야할 값보다 크면 너무 많이 벌목한 것
        s = mid + 1 # 기준 높이를 높임
    else: # 너무 조금 벌목한 경우
        e = mid - 1 # 기준 높이를 낮춤

print(e)
