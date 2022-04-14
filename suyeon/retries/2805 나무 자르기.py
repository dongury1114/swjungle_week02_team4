import sys

n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

s, e = 1, max(trees)
while s<=e:
    get_tree = 0
    mid = (s+e)//2
    for tree in trees:
        if tree >= mid:
            get_tree+=tree-mid

    if get_tree >= m:
        s = mid+1
    else:
        e = mid-1

print(e)