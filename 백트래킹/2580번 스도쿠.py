import sys
data = []
for i in range(9):
    data.append(list(map(int, sys.stdin.readline().split())))
oton = [i for i in range(1, 10)]
for i in range(len(data)):
    A = oton
    B = []
    for j in data[i]:
        if j in A:
            A.remove(j)
        else:
            B.append(j)
    if len(A) == 1:
        oton.replace(0,B[0])
    
        
    
