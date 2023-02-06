N = int(input())
nums = []
for i in range(len(str(N))):
    nums.append(int(str(N)[i]))
nums.sort(reverse = True)
for i in range(len(nums)):
    print(nums[i],end='')

