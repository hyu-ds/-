A = 'none'
while True:
    A = input()
    if A == '.':
        print('yes')
        break
    B = []
    
    for i in range(len(A)):
        if A[i] == ('('):
            B.append('(')
        elif A[i] == (')'):
            if len(B) == 0:
                print('no')
                break
            elif B[-1] == '(':
                del B[-1]
            else:
                print('no')
                break
        elif A[i] == ('['):
            B.append('[')
        elif A[i] == (']'):
            if len(B) == 0:
                print('no')
                break
            elif B[-1] == '[':
                del B[-1]
            else:
                print('no')
                break
        elif A[i]=='.' and len(B)==0:
            print('yes')
            break
        elif A[i]=='.' and len(B)!=0:
            print('no')
            break



