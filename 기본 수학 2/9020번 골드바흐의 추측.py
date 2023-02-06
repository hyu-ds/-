def sosu(n):
    lst = [i for i in range(2,n+1)]
    k = 0
    while k < len(lst):
        for i in lst:
            if i % lst[k] == 0 and i / lst[k] != 1:
                lst.remove(i) 
        k += 1
    return lst
T = int(input())

for i in range(T):
    can = []
    jaksu = int(input())
    for j in range(3,jaksu):
        if j in sosu(jaksu) and jaksu-j in sosu(jaksu):
            can.append([j,jaksu-j])
    if len(can) % 2 == 0:
        print(can[int(len(can)/2)][1],can[int(len(can)/2)][0])
    else:
        print(can[int((len(can)+1)/2)][1],can[int((len(can)+1)/2)][0])
            
        
