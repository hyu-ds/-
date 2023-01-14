def facto(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return facto(n-1) * n
num = int(input())
print(facto(num))