import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
M = int(input())
cl = list(map(int,input().split()))
ans = []
inter = set(cards) & set(cl)
for i in cl:
    if i in inter:
        ans.append(1)
    else:
        ans.append(0)
for i in ans:
    print(i,end=' ')