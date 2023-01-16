import sys
K = int(sys.stdin.readline())
di = []
le = []
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    di.append(a)
    le.append(b)
A = [0]*6
for i in range(len(di)):
    for j in range(len(di)):
        if di[i] == di[j]:
            A[i] += 1
big_sqaure = 1
small_sqaure = 1

for i in range(6):
    if A[i] == 1:
        big_sqaure = big_sqaure * le[i]
        small_sqaure = small_sqaure * le[i-3]

print((big_sqaure - small_sqaure)*K)
    
    



        
    



