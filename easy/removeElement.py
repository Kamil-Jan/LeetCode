class Solution:
    def removeDuplicates(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

