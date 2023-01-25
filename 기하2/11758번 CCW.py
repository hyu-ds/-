
px1, py1 = map(int, input().split())
px2, py2 = map(int, input().split())
px3, py3 = map(int, input().split())
cross = (px2-px1)*(py3-py2)-(px3-px2)*(py2-py1)
if cross > 0:
    print(1)
elif cross < 0:
    print(-1)
else:
    print(0)
