import sys

sys.stdin = open('input.txt')

N, M = map(int,input().split()) # 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))


end = max(trees) # 시작 점, 끝점

start, end = 0, max(trees)


# 이분 탐색
while start <= end:
    mid = (start+end)//2
    sum = 0 # 잘린 나무 합
    for i in trees:
        if i > mid: # mid보다 큰 나무 높이는 잘림
            sum += i - mid

    if sum >= M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)

# https://developoerty.tistory.com/31