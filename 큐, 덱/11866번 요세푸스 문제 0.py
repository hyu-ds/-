N, K = map(int,input().split())
from collections import deque
pointer = 0
cnt = 0
nums = deque([i+1 for i in range(N)])
ys = []
while len(nums) != 0:
    cnt += 1
    if cnt % K == 0:
        ys.append(nums[0])
        nums.popleft()
    else:
        left = nums[0]
        nums.popleft()
        nums.append(left)
print('<', end='')
for i in ys[:-1]:
    print(i,end=', ')
print(ys[-1],end='')
print('>')



    