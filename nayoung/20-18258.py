import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

q=deque()

def push(x):
    q.append(x)

def pop():
    if len(q) == 0:
        print('-1')
    else:
        print(q.popleft())

def size():
    print(len(q))

def empty():
    if len(q) == 0:
        print('1')
    else:
        print('0')

def front():
    if len(q) ==0:
        print('-1')
    else:
        print(q[0])

def back():
    if len(q) ==0:
        print('-1')
    else:
        print(q[-1])

for i in range(n):
    word=input().split()
    if word[0] == 'push':
        push(word[1])
    if word[0] == 'pop':
        pop()
    if word[0] == 'size':
        size()
    if word[0] == 'empty':
        empty()
    if word[0] == 'front':
        front()
    if word[0] == 'back':
        back()