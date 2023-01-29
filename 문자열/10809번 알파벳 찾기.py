S = input()

for i in range(97,123):
    for j in range(len(S)):
        a = 0
        if chr(i) == S[j]:
            print(j,end = ' ')
            a += 1
            break
    if a == 0:
        print(-1, end = ' ')

