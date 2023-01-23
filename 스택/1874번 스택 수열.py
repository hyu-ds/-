import sys
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline().strip()) for i in range(n)]
stack = []
pm = []
k = 0
i = 1
while k < n:
    if len(stack)==0:
        stack.append(i)
        pm.append('+')
        i += 1
    else:
        if stack[-1] != n_list[k]:
            stack.append(i)
            pm.append('+')
            i += 1 
        elif stack[-1] == n_list[k]:
            del stack[-1]
            pm.append('-')
            k +=1
    if len(stack)>0:
        if stack [-1]>n:
            print('NO')
            sys.exit()
print(*pm,sep='\n')
    


