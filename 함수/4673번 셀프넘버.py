def d(n):
    N = [int(i) for i in str(n)]
    return n + sum(N)
one_to_man = [0]*10000
A = []
for i in range(1,10001):
    if one_to_man[i-1] == 0:
        A.append(i)
    while d(i) <= 10000:
        a = d(i)
        one_to_man[a-1] = 1
        i = a
A.sort()
for i in A:
    print
    