K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    if num == 0:
        del stack[-1]
print(sum(stack))

