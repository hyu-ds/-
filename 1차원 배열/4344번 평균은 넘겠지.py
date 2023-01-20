C = int(input())
for _ in range(C):
    stu = list(map(int,input().split()))
    mean = sum(stu[1:])/len(stu[1:])
    a = 0
    for i in stu[1:]:
        if i > mean:
            a += 1
    k = round(a/(len(stu)-1)*100,3)
    print('%0.3f%%' %(k))