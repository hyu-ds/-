import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    data[i] = list(data[i][1], data[i][0])
data.sort()
for i in range(len(data)):
    print(str(data[i][1]) + ' ' + str(data[i][0]))
    