nums = [1,2,3]
nums2 = [4,5,6]
nums3 = [7,8,9]
nums4 = ["lists", 4]
print(nums4)
ans = [nums,nums2,nums3]
nums.append(3)
nums.remove(2)
nums.pop()
nums.insert(0,5)
nums.sort()
for x in nums:
    print(x)
print()
print(ans[2][2])