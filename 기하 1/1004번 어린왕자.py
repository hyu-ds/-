T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    num = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        one = (cx-x1)**2+(cy-y1)**2
        two = (cx-x2)**2+(cy-y2)**2
        if one < r**2 and two > r**2:
            num += 1
        elif one > r**2 and two < r**2:
            num += 1
    print(num)
