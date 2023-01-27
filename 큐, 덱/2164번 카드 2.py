import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque([i+1 for i in range(N)])
while len(q) != 1:
    del q[0]
    tmp = q[0]
    q.popleft()
    q.append(tmp)
print(q[0])