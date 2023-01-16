import sys
a = 1
while a != 0:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        sys.exit()
    print(a+b)
