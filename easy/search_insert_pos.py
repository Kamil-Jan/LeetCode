class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if nums == []:
            return 0
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)

