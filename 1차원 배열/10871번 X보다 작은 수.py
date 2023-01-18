N, X = map(int,input().split())
num_list = list(map(int,input().split()))
small_num = []
for i in num_list:
    if i < X:
        small_num.append(i)
    
for i in small_num:
    print(i,end=' ')

