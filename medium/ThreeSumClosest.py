from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dif = float("inf")
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                dif = target - three_sum
                if abs(dif) < abs(min_dif):
                    min_dif = dif
                    if min_dif == 0:
                        return target
                if three_sum < target:
                    low += 1
                else:
                    high -= 1
        return target - min_dif

