from typing import List


class Solution:
    def reverse(self, nums, low, high):
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = i = -1
        for j in range(len(nums) - 1):
            if nums[j] < nums[j + 1]:
                k = j
            if nums[j] > nums[k]:
                i = j
        if nums[-1] > nums[k]:
            i = len(nums) - 1

        if k == -1:
            self.reverse(nums, 0, len(nums) - 1)
        else:
            nums[k], nums[i] = nums[i], nums[k]
            self.reverse(nums, k + 1, len(nums) - 1)

