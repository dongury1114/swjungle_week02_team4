# 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성
# 그냥 주어지는 명령에 따라 코드 짜주면 된다.

import sys

input=sys.stdin.readline

n=int(input())

# arr = [input().strip() for i in range(n)]
#['push 1', 'push 2', 'top', 'size', 'empty', 'pop', 'pop', 'pop', 'size', 'empty', 'pop', 'push 3', 'empty', 'top']

stack = []

def push(x): #리스트의 마지막에 추가 (그 이하는 pop empty top같은 애들의 print임)
    stack.append(x) 

def pop():
    if len(stack) == 0:
        print('-1')
    else:
        print(stack.pop()) #print를 안 해주면 출력이 안돼

def size():
    print(len(stack))

def empty():
    if len(stack) == 0: #len()함수 써야되더라~~
        print('1')
    else:
        print('0')

def top():
    if len(stack) == 0:
        print('-1')
    else:
        print(stack[-1])

for i in range(n):
    word = input().split() #push 1 이런 애들 분리해주는 것 >> ['push', '1'] 이런형태로 들어가고, 그래서 word의[1]번째 요소를 출력해야하니까 저렇게 쓰는 거다~~
    if word[0] == 'push':
        push(word[1])
    if word[0] == 'pop':
        pop()
    if word[0] == 'size':
        size()
    if word[0] == 'empty':
        empty()
    if word[0] == 'top':
        top()