# 다시 풀어야 하는 문제...

import sys

input=sys.stdin.readline

g=input().strip() #strip 안 써주면 개행 되어서 출력됨

def checkG(Bracket): # '올바른' 괄호인지 확인하는 작업 == 만약 stack 리스트가 비워지지 않는다면 짝이 맞지 않은 괄호라는 거임.
    stack=[]
    for i in Bracket:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' and stack: #and 연산자는 앞이 거짓이라면 뒤는 확인하지도 않고 앞 값을 리턴해준다.
            if stack[-1] == '(':
                stack = stack[:-1] # -1의 위치까지 슬라이싱. 즉, 뒤에 1개 제외
            else:
                stack.append(i)
        elif i == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(i)
        else:
            stack.append(i)
    
    if stack:
        return False # 안 맞는 애들이면 64줄의 0 출력하러 ㄱㄱ
    else:
        return True # 올바른 괄호(짝 맞는)면 연산하러 ㄱㄱ

def sumG(Bracket): #계산하는 작업
    stack=[]
    for i in Bracket:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack[-1]=2 # () 맞물리면 == 2 정수 넣어버려~
            else: # 괄호가 맞지 않으면 연산해버려서 stack 안에 연산한 정수를 넣어둠.
                tmp = 0
                for j in range(len(stack)-1,-1,-1):
                    if stack[j] == '(':
                        stack[-1] = tmp*2
                        break
                    else:
                        tmp+=stack[j]
                        stack = stack[:-1]
        elif i == ']':
            if stack[-1] == '[':
                stack[-1]=3 # [] == 3
            else: #[-1]이랑 괄호가 맞지 않을때
                tmp=0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == '[':
                        stack[-1]=tmp*3
                        break
                    else:
                        tmp+=stack[i]
                        stack=stack[:-1]
    return sum(stack) #stack에 있는 값 sum하고

if checkG(g) == False:
    print(0)
else:
    print(sumG(g)) #61줄에서 반환된 값 출력