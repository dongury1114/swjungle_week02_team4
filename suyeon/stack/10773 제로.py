import sys
k = int(sys.stdin.readline().strip())

A = []
for _ in range(k):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        A.pop()
    else:
        A.append(temp)

print(sum(A))