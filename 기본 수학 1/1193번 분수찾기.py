import sys
num = int(input())
if num == 1 :
    print("1/1")
    sys.exit()
n1 = 1
n2 = 1
n3 = 1

while num > n2:
    n1 = n1 + 1
    n2 = n2 + n1
    n3 += 1
if n3 % 2 == 0:    
    bj = num - (n2 -  n1)
    bm = n3 + 1 - bj
if n3 % 2 == 1:
    bm = num - (n2 -  n1)
    bj = n3 + 1 - bm
bj = str(bj)
bm = str(bm)    
print(bj+'/'+bm)
