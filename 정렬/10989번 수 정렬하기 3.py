import sys
N = int(sys.stdin.readline())
zeros = [0] * 10001

for i in range(N):
    A = int(sys.stdin.readline())
    zeros[A] += 1
for i in range(len(zeros)):
    for j in range(zeros[i]):
        print(i)

