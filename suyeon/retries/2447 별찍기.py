# retry
import sys
sys.setrecursionlimit(10**6)

def star(x):
    if x == 1:
        return ['*']

    Stars = star(x//3)
    L = []

    for s in Stars:
        L.append(s*3)
    for s in Stars:
        L.append(s+' '*(x//3)+s)
    for s in Stars:
        L.append(s*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))