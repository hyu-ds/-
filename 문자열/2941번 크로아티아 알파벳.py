word = str(input())
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in range(len(word)):
    if word[i] == '=':
        if i >= 1:
            if word[i-1] == 'c'or word[i-1] == 's'or word[i-1]=='z':
                if i >= 2:
                    if word[i-2] == 'd':
                        cnt += 1
                else:
                    cnt += 1

    elif word[i] == '-':
    elif word[i] == 'j':
    

    
    
