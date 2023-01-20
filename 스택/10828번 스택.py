import sys
stack = []
def push(X):
        stack.append(X)
def pop():
    if len(stack) == 0:
        print(-1) 
    else: 
        print(stack[-1])
        del stack[-1]
def size():
    print(len(stack))
def empty():
    if len(stack) != 0:
        print(0)
    if len(stack) == 0:
        print(1)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
N = int(input())
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        push(int(a[1]))
    if a[0] == 'pop':
        pop()
    if a[0] == 'size':
        size()
    if a[0] == 'empty':
        empty()
    if a[0] == 'top':
        top()

    
