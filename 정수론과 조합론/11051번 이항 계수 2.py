N, K = map(int,input().split())
ans = 1
for i in range(N-K+1,N+1):
    ans = int(ans * i)
for i in range(1,K+1):
    ans = int(ans // i)

print(int(int(ans)%10007))