import sys
N = int(sys.stdin.readline())
A = []
B = {}
for _ in range(N):
    a = int(sys.stdin.readline())
    A.append(a)
for i in range(len(A)):
    if A[i] not in B:
        B[A[i]] = 1
    if A[i] in B:
        B[A[i]] += 1        
max(B.values())
print(sum(A)/len(A))
print(int(A[(N+1)/2]))
print()
print(A[-1]-A[0])
