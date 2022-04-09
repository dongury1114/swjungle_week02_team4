import sys

class Stack:
    def __init__(self):
        self.items = [] # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try: # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError: # indexError 발생
            return -1 # 스택이 비었으면 -1

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1 # 스택이 비었으면 -1

    def __len__(self): # len()로 호출하면 stack의 item 수 반환
        return len(self.items)

    def isEmpty(self):
        if len(self) == 0: # 비어있으면 1
            return 1
        return 0 # 아니면 0

n = int(sys.stdin.readline().strip())
A = Stack()
for _ in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        A.push(order[1])
    elif order[0] == 'top':
        print(A.top())
    elif order[0] == 'size':
        print(len(A))
    elif order[0] == 'empty':
        print(A.isEmpty())
    elif order[0] == 'pop':
        print(A.pop())