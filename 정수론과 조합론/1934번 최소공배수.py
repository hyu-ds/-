T = int(input())
for i in range(T):
    n1, n2 = map(int,input().split())
    if n1 > n2:
        big = n1
        small = n2
    else:
        big = n2
        small = n1
    csgbs = big
    tf = True
    while tf == True:
        if big % small == 0:
            print(big)
            break
        if csgbs % small == 0:
            csgbs += small
            if csgbs % big == 0:
                print(csgbs)
                break
        else:
            csgbs += 1
