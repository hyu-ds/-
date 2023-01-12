import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort()
for i in range(len(data)):
    print(str(data[i][0]) + ' ' + str(data[i][1]))
    
    


