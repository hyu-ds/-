remains = []
for _ in range(10):
    a = int(input())
    b = a % 42
    remains.append(b)
dif = set(remains)
print(len(dif))
