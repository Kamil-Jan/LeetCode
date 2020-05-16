class Solution:
    def removeDuplicates(self, nums):
        i = 0
        if len(nums) == 0:
            return 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

x = Solution()
print(x.removeDuplicates([1,2,2,3]))
