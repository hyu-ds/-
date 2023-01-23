def d(n):
    N = [int(i) for i in str(n)]
    return n + sum(N)
one_to_man = [0]*10000

for i in range(1,10001):
    if one_to_man[i-1] == 0:
        one_to_man[i-1] = 2
    while d(i) <= 10000:
        a = d(i)
        one_to_man[a-1] = 1
        i = a
for i in range(len(one_to_man)):
    if one_to_man[i] == 2:
        print(i+1)