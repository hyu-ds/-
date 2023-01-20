N = int(input())
former = list(map(int,input().split()))
Later = []
M = max(former)
for i in former:
    i = i/M * 100
    Later.append(i)
print(sum(Later)/len(Later))