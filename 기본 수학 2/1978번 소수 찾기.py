def sosu(n):
    lst = [i for i in range(2,n+1)]
    k = 0
    while k < len(lst):
        for i in lst:
            if i % lst[k] == 0 and i / lst[k] != 1:
                lst.remove(i) 
        k += 1
    return lst
N = int(input())
nums = list(map(int, input().split()))
ss = 0
for i in nums:
    if i in sosu(1000):
        ss += 1
print(ss)

    



    
