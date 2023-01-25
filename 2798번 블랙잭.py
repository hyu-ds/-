from itertools import combinations
N, M = map(int, input().split())
card = list(map(int, input().split()))
Max = 0
com = list(combinations(card,3))
for i in range(len(com)):
    a = sum(com[i])
    if a <= M:
        if a > Max:
            Max = a
print(Max)