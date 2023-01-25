def star(k):
    if k == 1:
        return '*'
    for _ in range(int(k-1)):
        print(star(int(k/3)),end= '')
    print(star(int(k/3)))
    print(star(int(k/3)),end = '')
    print(' '*(int(k/3)),end='')
    print(star(int(k/3)))
    for _ in range(k):
        print(star(int(k/3)),end= '')
N = int(input())
star(int(N))



