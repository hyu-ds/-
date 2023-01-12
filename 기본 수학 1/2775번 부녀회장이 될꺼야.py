nums = dict()
def bnhj(k,n):
    if (k,n) in nums:
        return nums[(k,n)]
    if n == 1:
        return 1
    if k == 0:
        return n
    sum = bnhj(k-1,n) + bnhj(k,n-1)
    return bnhj(k-1,n) + bnhj(k,n-1)
    nums[(k,n)] = sum
import sys
T = int(input())
for i in range(T):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(bnhj(a, b))
