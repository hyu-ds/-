N, K = map(int,input().split())
ans = 1
for i in range(1,N+1):
    ans = ans * i
for i in range(1,K+1):
    ans = ans / i
for i in range(1,N-K+1):
    ans = ans / i
print(int(ans))