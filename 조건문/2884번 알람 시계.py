H, M = map(int, input().split())
if H >= 1:
    if M >= 45:
        print(str(H)+' '+str(M-45))
    if M < 45:
        print(str(H-1)+' '+str(M+15))
else:
    if M >= 45:
        print(str(H)+' '+str(M-45))
    if M < 45:
        print(str(23)+' '+str(M+15))