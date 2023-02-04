import sys
N, M = map(int,input().split())
input = sys.stdin.readline
S = set()
SS = []
cnt = 0
for i in range(N):
    st = input()
    S.append(st)
for i in range(M):
    st = input()
    SS.append(st)
for i in SS:
    if i in S:
        cnt += 1
print(cnt)

