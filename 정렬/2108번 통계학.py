N = int(input())
nums = []
can = []
for i in range(N):
    nums.append(int(input()))
nums.sort()
cnt = [0] * 8001
for i in range(len(nums)):
    cnt[nums[i]+4000] += 1
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        can.append(i-4000)
can.sort()
print(round(sum(nums)/len(nums)))
print(nums[int((len(nums)+1)/2)-1])
if len(can) != 1:
    print(can[1])
else:
    print(can[0])
print(nums[-1]-nums[0])