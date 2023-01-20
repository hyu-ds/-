word = input().upper()
alpha = dict()
for i in range(len(word)):
    if word[i] in alpha:
        alpha[word[i]] += 1
    if word[i] not in alpha:
        alpha[word[i]] = 1
A = list(alpha.values()).sort()
B = []
for i in range(len(alpha)):
    if alpha.get(word[i]) == A[0]:
        B.append(alpha[i])
print(B)


    

