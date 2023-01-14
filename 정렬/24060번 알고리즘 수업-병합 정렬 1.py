def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        
def merge(A, p, q, r):
    i = p
    j = q+1
    tmp = []
    while (i<=q and j<=r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            i = i+1
        else:
            tmp.append(A[j])
            j = j+1
    while i <= q:
        tmp.append(A[i])
        i = i+1
    while j <= r:
        tmp.append(A[j])
        j = j+1
    i = p
    t = 0
    print(tmp)
    while i <= r:
        A[i] = tmp[t]
        i = i+1
        t = t+1 
        
merge_sort([4,5,1,3,2],0,4)
import sys
N, K = int(sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
