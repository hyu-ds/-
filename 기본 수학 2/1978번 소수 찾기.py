N = int(input())
nums = list(map(int, input().split()))
ss = []
for i in nums:
    if i == 2:
        ss.append(i)
    else:
        for j in range(2,i):
            if i % j != 0:
                ss.append(i)
            else:
                
print(len(ss))
