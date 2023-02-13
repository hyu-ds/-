from fractions import Fraction
N = int(input())
num = list(map(int,input().split()))
ans = []
for i in range(len(num)-1):
    ans.append(num[0]/num[i+1])
for i in range(1,len(ans)+1):
    
    if num[0]/num[i] % 1 != 0:
        print(Fraction(num[0],num[i]))
    else:
        print(str(int(num[0]/num[i]))+'/1')
    

    
