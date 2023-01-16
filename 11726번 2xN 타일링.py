import sys
cache = dict()
def tile(n):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        cache[n] = tile(n-1)+tile(n-2)
        return (tile(n-1)+tile(n-2))
    
N = int(sys.stdin.readline())
print(tile(N)%10007)