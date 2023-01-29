word = input().upper()
alpha = [chr(i) for i in range(65,91)]
num = [0]*26
for i in range(len(word)):    
    for j in range(len(alpha)):
        if word[i] == alpha[j]:
            num[j] += 1
M = max(num)
Mn = 0
for i in num:
    if i == M:
        Mn += 1
if Mn == 1:
    print(alpha[num.index(M)])
else:
    print('?')




    

