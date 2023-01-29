import sys
N = int(input())
M = N
k = 2
while N >= k:
    if M % k == 0:
        M = M / k
        print(k)
        if M == 1:
            sys.exit()
    else:
        k += 1


