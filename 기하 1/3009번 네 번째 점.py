import sys
a, b = map(int, sys.stdin.readline().split())
s, d = map(int, sys.stdin.readline().split())
e, f = map(int, sys.stdin.readline().split())
x_ = [a, s, e]
y_ = [b, d, f]
for i in range(len(x_)):
    for j in x_[i+1:]:
        if x_[i] == j:
            x_.remove(x_[i])
            x_.remove(j)
            break
for i in range(len(y_)):
    for j in y_[i+1:]:
        if y_[i] == j:
            y_.remove(y_[i])
            y_.remove(j)
            break
print(x_[0], y_[0])