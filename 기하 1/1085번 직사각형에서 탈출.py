import sys
x, y, w, h = map(int, sys.stdin.readline().split())
length = [x, y, w-x, h-y]
print(min(length))