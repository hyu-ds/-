N = int(input())
for _ in range(N):
    A = 0
    B = 0
    a = input()
    for i in range(len(a)):
        if a[i] == ('('):
            A += 1
        if a[i] == (')'):
            B += 1
        if A < B:
            print('NO')
            break
    if A == B:
        print('YES')
    if A > B:
        print('NO')

    


