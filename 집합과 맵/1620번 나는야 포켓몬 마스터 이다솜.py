M, N = map(int,input().split())
idx = {}
num = {}
for i in range(1,M+1):
    A = input()
    idx[i] = A
    num[A] = i
for i in range(N):
    A = input()
    try:
        print(idx[int(A)])
    except:
        print(num[A])
        

