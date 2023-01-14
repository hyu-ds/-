def hanoi1(n):
    if n == 1:
        return 1  
    else:
        return hanoi1(n-1)*2 + 1
def hanoi2(n):
    if n == 1:
        A = [[1,3]]
        return [A[0][0], A[0][1]]
    else:
        A = hanoi2(n-1)
        B = A
        C = A
        D = []
        E = [0]*len(A)
        F = [0]*len(A)
        for i in B:
            for index, value in enumerate(B):
                if value == 3:
                    B[index] = 2
                    E[index] = 1
                if value == 2 and E[index] != 1:
                    B[index] = 3
        for i in C:
            for index, value in enumerate(C):
                if value == 1:
                    C[index] = 2
                    F[index] = 1
                if value == 2 and F[index] != 1:
                    C[index] = 1
        for i in B:
            D.append(i)
        D.append([1,3])
        for i in C:
            D.append(i)    

        return D

K = int(input())
print(hanoi1(K))
print(hanoi2(K))

