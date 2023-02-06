N = int(input())
nums = []
ans = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
for i in range(2,nums[1]):
    k = 0
    for j in range(len(nums)):
        if j+1 < len(nums):
            re = nums[j] % i
            re2 = nums[j+1] % i
            if re == re2:
                k += 1
            else:
                break
            if k == len(nums)-1:
                ans.append(i)
for i in ans:
    print(i,end=' ')


