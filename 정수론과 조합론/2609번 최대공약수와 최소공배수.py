a, b = map(int,input().split())
if a < b:
    small = a
    big = b
else:
    small = b
    big = a
cdgys = 0
csgbs = 0
for i in range(1, small+1):
    if a % i == 0 and b % i == 0 and i > cdgys:
        cdgys = i
j = True
csgbs = big
while j == True:
    if csgbs % a == 0 and csgbs % b == 0:
        j = False
        break
    csgbs += 1
print(cdgys)
print(csgbs)



