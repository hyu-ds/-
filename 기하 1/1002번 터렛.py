T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x2-x1)**2 + (y2-y1)**2
    sum = (r1 + r2)**2
    sub = (r1 - r2)**2
    if x1 == x2 and y1 == y2 and asr1==r2:
        print(-1)
    elif sum == dist or  dist == sub:
        print(1)
    elif sum > dist and dist > sub:
        print(2)
    else:
        print(0)
    
