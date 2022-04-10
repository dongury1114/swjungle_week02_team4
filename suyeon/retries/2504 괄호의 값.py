import sys
s = sys.stdin.readline().strip()

stack = []
tmp = 1
answer = 0
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            answer=0
            break
        if s[i-1] == '(': # 괄호 안에 다른 괄호가 없으면 더하기만 하면 됨
            answer += tmp
        tmp //= 2
        stack.pop()
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            answer=0
            break
        if s[i-1] == '[': # 괄호 안에 다른 괄호가 없으면 더하기만 하면 됨
            answer+=tmp
        tmp//=3 
        stack.pop()    
        
if stack:
    print(0)
else:
    print(answer)
    