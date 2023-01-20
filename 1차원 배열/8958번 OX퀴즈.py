N = int(input())
OXes = []
for _ in range(N):
    A = input()
    OXes.append(A)

for i in range(len(OXes)):
    total = 0
    a = 0
    for j in range(len(OXes[i])):
        if OXes[i][j] == 'O':
            a += 1
            total += a
        else:
            a = 0
    print(total)

