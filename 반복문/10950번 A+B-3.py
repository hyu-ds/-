T = int(input())
a = []
b = []
for _ in range(T):
    A, B = map(int,input().split())
    a.append(A)
    b.append(B)
for i in range(len(a)):
    print(a[i]+b[i])

