import sys

def VPS(s):
    left = []
    right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left.append(s[i])
        else:
            right+=1
            if len(left)>0:
                left.pop()
                right -= 1
            else:
                return 'NO'
    if right>0 or len(left)>0:
        return 'NO'
    else:
        return 'YES'


t = int(sys.stdin.readline().strip())
for i in range(t):
    print(VPS(list(sys.stdin.readline().strip())))