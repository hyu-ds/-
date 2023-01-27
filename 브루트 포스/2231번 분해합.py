N = int(input())
A = [i for i in range(1,N)]
min = 1000000
for i in range(len(A)):
    bhh = i+sum([int(i) for i in str(i)])
    if bhh == N:
        min = i
        break
if min == 1000000:
    print(0)
else:
    print(min)

