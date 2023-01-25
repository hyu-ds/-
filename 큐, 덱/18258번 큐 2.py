import sys
from collections import deque
que = deque()
def push(X):
    que.append(X)
def pop():
    if len(que)>0:
        print(que.popleft())
    else:
        print(-1)
def size():
    print(len(que))
def empty():
    if len(que) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(que)==0:
        print(-1)
    else:
        print(que[0])
def back():
    if len(que)==0:
        print(-1)
    else:
        print(que[-1])
N = int(sys.stdin.readline())
for i in range(N):
    a = sys.stdin.readline().strip()
    if 'push' in a:
        push(a[5:]) 
    if a =='pop':
        pop()
    if a =='size':
        size()
    if a =='empty':
        empty()
    if a =='front':
        front()
    if a =='back':
        back()


