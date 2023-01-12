import sys
data = []
big = []
X = 0
Y = 0
Max = -1
for i in range(9):
    data.append(list(map(int,sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if data[i][j] > Max:
            Max = data[i][j]
            X = i + 1
            Y = j + 1
print(Max)
print(X, Y)
            
