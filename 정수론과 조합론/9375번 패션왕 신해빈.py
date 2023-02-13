import math
T = int(input())
for _ in range(T):
    n = int(input())
    clothes = [0] * 30
    type = []
    for _ in range(n):
        a, b = input().split()
        if b not in type:
            type.append(b)
        clothes[type.index(b)] += 1
    ans = 1
    for i in range(len(clothes)):
        if clothes[i] != 0:
            ans = ans * (clothes[i]+1)
    print(ans-1)
    

