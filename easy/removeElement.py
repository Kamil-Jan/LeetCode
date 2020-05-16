class Solution:
    def removeDuplicates(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

x = Solution()
print(x.removeDuplicates([3,2,2,3,3], 3))

